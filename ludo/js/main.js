/**
 * main.js
 * App entry point.
 *   1. Manages the setup screen (player name + type config).
 *   2. On "Start Game": bootstraps TurnManager, Renderer, EventHandler.
 *
 * No game logic lives here — only UI state for the pre-game setup.
 */

(function () {
  const MIN_PLAYERS = 2;
  const MAX_PLAYERS = 4;

  /* Default two-player config shown on load */
  let _configs = [
    { name: 'Player 1', type: 'green'  },
    { name: 'Player 2', type: 'orange' },
  ];

  /* ─── Boot ─────────────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', () => {
    _renderRows();
    document.getElementById('add-player-btn').addEventListener('click', _addPlayer);
    document.getElementById('start-game-btn').addEventListener('click', _startGame);
  });

  /* ─── Add / remove players ─────────────────────────────────────── */
  function _addPlayer() {
    if (_configs.length >= MAX_PLAYERS) return;
    /* Alternate default types so each new player has a different type */
    const type = _configs.length % 2 === 0 ? 'green' : 'orange';
    _configs.push({ name: `Player ${_configs.length + 1}`, type });
    _renderRows();
  }

  function _removePlayer(idx) {
    _configs.splice(idx, 1);
    _renderRows();
  }

  /* ─── Render setup rows ─────────────────────────────────────────── */
  function _renderRows() {
    const list = document.getElementById('player-config-list');
    list.innerHTML = '';

    _configs.forEach((cfg, i) => {
      const row = document.createElement('div');
      row.className = 'setup-row';

      row.innerHTML = `
        <input
          type="text"
          class="setup-name"
          data-idx="${i}"
          value="${_esc(cfg.name)}"
          placeholder="Player name"
          maxlength="20"
        />
        <div class="type-toggle">
          <button
            class="type-btn ${cfg.type === 'green' ? 'active' : ''}"
            data-idx="${i}" data-type="green">🟢 Green</button>
          <button
            class="type-btn ${cfg.type === 'orange' ? 'active' : ''}"
            data-idx="${i}" data-type="orange">🟠 Orange</button>
        </div>
        ${_configs.length > MIN_PLAYERS
          ? `<button class="remove-btn" data-idx="${i}" title="Remove">✕</button>`
          : ''}
      `;

      /* Name input */
      row.querySelector('.setup-name').addEventListener('input', e => {
        _configs[+e.target.dataset.idx].name = e.target.value.trim() || `Player ${i + 1}`;
      });

      /* Type toggle buttons */
      row.querySelectorAll('.type-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          _configs[+btn.dataset.idx].type = btn.dataset.type;
          _renderRows();
        });
      });

      /* Remove button (only shown when > MIN_PLAYERS) */
      row.querySelector('.remove-btn')?.addEventListener('click', () => _removePlayer(i));

      list.appendChild(row);
    });

    /* Disable "Add Player" when at max */
    document.getElementById('add-player-btn').disabled = _configs.length >= MAX_PLAYERS;
  }

  /* ─── Start game ─────────────────────────────────────────────────── */
  function _startGame() {
    /* Read latest name values from inputs (user may not have blurred) */
    document.querySelectorAll('.setup-name').forEach((inp, i) => {
      _configs[i].name = inp.value.trim() || `Player ${i + 1}`;
    });

    /* Swap screens */
    document.getElementById('setup-screen').hidden = true;
    document.getElementById('game-layout').hidden  = false;

    /* Re-render the SVG overlay now that the board is visible */
    requestAnimationFrame(renderOverlay);

    /* Bootstrap engine */
    TurnManager.startGame(_configs);

    /* Initial UI state */
    const state = TurnManager.getState();
    Renderer.renderPlayerCards(state.players, state.currentPlayerIndex);
    Renderer.renderDice(null);

    const first = TurnManager.getCurrentPlayer();
    Renderer.setStatus(`${first.name}'s turn — click Roll Dice`);
    Renderer.appendLog('Game started!');

    /* Wire button events */
    EventHandler.init();
  }

  /* ─── Escape helper ──────────────────────────────────────────────── */
  function _esc(str) {
    return str.replace(/[&<>"']/g, c =>
      ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])
    );
  }
})();
