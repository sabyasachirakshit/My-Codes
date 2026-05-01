/**
 * EventHandler.js
 * Wires the "Roll Dice" button to the TurnManager + Renderer pipeline.
 *
 * Animation sequence on each click:
 *   1. Disable button, call TurnManager.roll()
 *   2. Show dice value with shake animation
 *   3. After DICE_DELAY ms → call TurnManager.move()
 *   4. Call Renderer.animateMove() — token flies to 'landed' tile
 *      If snake/ladder: tile flashes, then token flies to 'to' tile
 *   5. In onComplete callback → update player cards, log the event
 *   6. If winner → show win overlay; else re-enable button for next player
 */

const EventHandler = (() => {
  const DICE_DELAY = 550; /* ms between dice display and token movement */

  let _locked = false;

  /* ─── init ───────────────────────────────────────────────────── */
  function init() {
    document.getElementById('roll-btn').addEventListener('click', _onRollClick);
  }

  /* ─── Roll click handler ─────────────────────────────────────── */
  function _onRollClick() {
    if (_locked) return;
    _lock(true);

    /* Step 1: roll the dice */
    const rollEvent = TurnManager.roll();
    const { player, diceValue } = rollEvent;

    /* Step 2: show dice + status */
    Renderer.renderDice(diceValue);
    Renderer.setStatus(`${player.name} rolled a ${diceValue}…`);

    /* Step 3: wait, then move */
    setTimeout(() => {
      const moveEvent = TurnManager.move();
      _applyMoveEvent(moveEvent);
    }, DICE_DELAY);
  }

  /* ─── Apply a move event (animates + updates UI) ─────────────── */
  function _applyMoveEvent(evt) {
    const { player, diceValue, from, landed, to, effect, direction, isWin } = evt;

    Renderer.animateMove(player, from, landed, to, () => {
      /* Fetch updated state (positions changed) */
      const state = TurnManager.getState();
      Renderer.renderPlayerCards(state.players, state.currentPlayerIndex);

      /* Build log entry */
      const arrow = direction === 'up' ? '⬆' : direction === 'down' ? '⬇' : '';
      let msg = `${player.name} rolled ${diceValue}: ${from || 'start'} → ${landed}`;
      if (effect) msg += `  ${effect} ${arrow} → ${to}`;
      Renderer.appendLog(msg, effect || '');

      if (isWin) {
        Renderer.appendLog(`🏆 ${player.name} wins!`, 'win');
        Renderer.setStatus(`${player.name} wins! 🎉`);
        Renderer.showWinner(player);
        /* Button stays disabled — game is over */
      } else {
        const next = TurnManager.getCurrentPlayer();
        Renderer.setStatus(`${next.name}'s turn — click Roll Dice`);
        _lock(false);
      }
    });
  }

  /* ─── Lock / unlock the roll button ─────────────────────────── */
  function _lock(locked) {
    _locked = locked;
    document.getElementById('roll-btn').disabled = locked;
  }

  return Object.freeze({ init });
})();
