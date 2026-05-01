/**
 * Renderer.js
 * All DOM read/write for the live game.
 * Receives plain data objects from TurnManager events — never calls game logic.
 *
 * Public surface:
 *   placeToken(player, tileNum)
 *   animateMove(player, from, landed, to, onComplete)
 *   renderDice(value)
 *   renderPlayerCards(players, currentIndex)
 *   setBoardGlow(playerType)
 *   setStatus(msg)
 *   appendLog(msg, modifier)
 *   showWinner(player)
 */

const Renderer = (() => {

  /* ─── DOM shortcuts ──────────────────────────────────────────── */
  const $board  = () => document.getElementById('board');
  const $tile   = n  => document.querySelector(`[data-tile="${n}"]`);
  const $token  = id => document.querySelector(`.token[data-player-id="${id}"]`);

  /* ─── Token element ──────────────────────────────────────────── */
  function _makeToken(player) {
    const el = document.createElement('div');
    el.className = `token ${player.type}`;
    el.dataset.playerId = player.id;
    el.title = player.name;
    return el;
  }

  /* ─── placeToken ─────────────────────────────────────────────── */
  /**
   * Instantly places a player's token on a tile.
   * Removes any existing token for that player first.
   * tileNum === 0 means off-board (token is removed but not placed).
   */
  function placeToken(player, tileNum) {
    const existing = $token(player.id);
    if (existing) existing.remove();
    if (tileNum === 0) return;

    const tile = $tile(tileNum);
    if (!tile) return;

    const token = _makeToken(player);
    tile.querySelector('.tile-tokens').appendChild(token);

    /* Brief landing animation */
    token.classList.add('token--land');
    token.addEventListener('animationend', () => token.classList.remove('token--land'), { once: true });
  }

  /* ─── animateMove ────────────────────────────────────────────── */
  /**
   * Smoothly moves a token from → landed → to.
   *   - from:   tile before the roll  (0 = off-board)
   *   - landed: tile after dice, before snake/ladder effect
   *   - to:     final tile after effect  (may equal landed)
   * Calls onComplete() once all animation is done.
   */
  function animateMove(player, from, landed, to, onComplete) {
    if (from === 0) {
      /* First move: no from-tile exists, just place */
      placeToken(player, to);
      onComplete();
      return;
    }

    _flyTo(player, from, landed, () => {
      if (landed === to) {
        /* No snake/ladder — done */
        onComplete();
        return;
      }

      /* Flash the landed tile to signal the effect trigger */
      const landedEl = $tile(landed);
      if (landedEl) {
        landedEl.classList.add('tile--effect-flash');
        landedEl.addEventListener('animationend',
          () => landedEl.classList.remove('tile--effect-flash'),
          { once: true }
        );
      }

      /* Brief pause so the flash is visible, then fly to final pos */
      setTimeout(() => _flyTo(player, landed, to, onComplete), 380);
    });
  }

  /**
   * Animates a single flight leg: from fromTile to toTile.
   * Creates a temporary flying token, transitions it, then places
   * the real token at toTile and removes the flying element.
   */
  function _flyTo(player, fromTile, toTile, onComplete) {
    const board     = $board();
    const boardRect = board.getBoundingClientRect();
    const bLeft     = boardRect.left + board.clientLeft; /* strip border */
    const bTop      = boardRect.top  + board.clientTop;
    const bW        = board.clientWidth;
    const bH        = board.clientHeight;

    const fromEl = $tile(fromTile);
    const toEl   = $tile(toTile);
    if (!toEl) { placeToken(player, toTile); onComplete(); return; }

    /* Calculate SVG-space centres (pixels relative to board content area) */
    const fr = fromEl ? fromEl.getBoundingClientRect()
                      : { left: bLeft, top: bTop + bH, width: 0, height: 0 };
    const tr = toEl.getBoundingClientRect();

    const startX = (fr.left + fr.width  / 2) - bLeft;
    const startY = (fr.top  + fr.height / 2) - bTop;
    const endX   = (tr.left + tr.width  / 2) - bLeft;
    const endY   = (tr.top  + tr.height / 2) - bTop;

    /* Hide the real token while the clone flies */
    const real = $token(player.id);
    if (real) real.style.opacity = '0';

    /* Create flying clone */
    const fly = _makeToken(player);
    fly.classList.add('token--flying');
    fly.style.left      = `${startX}px`;
    fly.style.top       = `${startY}px`;
    fly.style.transform = 'translate(-50%, -50%)';
    board.appendChild(fly);

    /* Trigger transition in next two frames (ensures initial paint) */
    requestAnimationFrame(() => requestAnimationFrame(() => {
      fly.style.left = `${endX}px`;
      fly.style.top  = `${endY}px`;
    }));

    fly.addEventListener('transitionend', () => {
      fly.remove();
      placeToken(player, toTile); /* restores real token with land animation */
      onComplete();
    }, { once: true });
  }

  /* ─── renderDice ─────────────────────────────────────────────── */
  /**
   * Shows the rolled value and plays the shake animation.
   * Passing null resets it to the idle emoji.
   */
  function renderDice(value) {
    const el = document.getElementById('dice');
    el.textContent = value ?? '🎲';
    if (value !== null) {
      el.classList.remove('dice--rolling');
      void el.offsetWidth; /* force reflow to restart animation */
      el.classList.add('dice--rolling');
      el.addEventListener('animationend',
        () => el.classList.remove('dice--rolling'),
        { once: true }
      );
    }
  }

  /* ─── renderPlayerCards ──────────────────────────────────────── */
  /**
   * Re-renders all player cards, highlighting the active player.
   * Also updates the board border glow to match the active player.
   */
  function renderPlayerCards(players, currentIndex) {
    const list = document.getElementById('players-list');
    list.innerHTML = '';

    players.forEach((p, i) => {
      const active = i === currentIndex;
      const card = document.createElement('div');
      card.className = [
        'player-card',
        `player-card--${p.type}`,
        active ? 'player-card--active' : '',
      ].join(' ').trim();

      const pos = p.position > 0 ? `Tile ${p.position}` : 'Start';
      card.innerHTML = `
        <div class="player-card__dot ${p.type}"></div>
        <div class="player-card__info">
          <strong>${_esc(p.name)}</strong>
          <span>${p.type === 'green' ? 'Climbs ladders' : 'Climbs snakes'}</span>
        </div>
        <div class="player-card__pos">${pos}</div>
      `;
      list.appendChild(card);
    });

    if (players[currentIndex]) {
      setBoardGlow(players[currentIndex].type);
    }
  }

  /* ─── setBoardGlow ───────────────────────────────────────────── */
  function setBoardGlow(playerType) {
    const board = $board();
    board.classList.remove('glow--green', 'glow--orange');
    board.classList.add(`glow--${playerType}`);
  }

  /* ─── setStatus ──────────────────────────────────────────────── */
  function setStatus(msg) {
    document.getElementById('status-msg').textContent = msg;
  }

  /* ─── appendLog ──────────────────────────────────────────────── */
  /**
   * Prepends an entry to the event log (newest on top).
   * modifier: '' | 'snake' | 'ladder' | 'win'  → sets log-entry--X class
   */
  function appendLog(msg, modifier = '') {
    const log = document.getElementById('game-log');
    const entry = document.createElement('div');
    entry.className = `log-entry${modifier ? ` log-entry--${modifier}` : ''}`;
    entry.textContent = msg;
    log.prepend(entry);
    while (log.children.length > 25) log.lastChild.remove();
  }

  /* ─── showWinner ─────────────────────────────────────────────── */
  function showWinner(player) {
    const icon = player.type === 'green' ? '🟢' : '🟠';
    const overlay = document.createElement('div');
    overlay.className = 'win-overlay';
    overlay.innerHTML = `
      <div class="win-card">
        <div class="win-icon">${icon}</div>
        <h2>${_esc(player.name)} Wins!</h2>
        <p>Reached tile 100 🎉</p>
        <button onclick="location.reload()">Play Again</button>
      </div>
    `;
    document.body.appendChild(overlay);
  }

  /* ─── Escape helper ──────────────────────────────────────────── */
  function _esc(str) {
    return str.replace(/[&<>"']/g, c =>
      ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])
    );
  }

  return Object.freeze({
    placeToken,
    animateMove,
    renderDice,
    renderPlayerCards,
    setBoardGlow,
    setStatus,
    appendLog,
    showWinner,
  });
})();
