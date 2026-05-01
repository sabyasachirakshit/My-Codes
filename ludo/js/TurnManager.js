/**
 * TurnManager.js
 * Main game-engine API. Orchestrates the two-step turn cycle:
 *
 *   roll()  →  move()  →  roll()  →  move()  →  …
 *
 * Each public method returns a plain event object — the DOM/renderer
 * layer will subscribe to these to drive animations and UI updates.
 * No DOM references exist in this file.
 *
 * ─── Turn state machine ──────────────────────────────────────────
 *
 *   [game not started]
 *        │  startGame()
 *        ▼
 *   waiting_roll  ──── roll() ────►  waiting_move
 *        ▲                                │
 *        └──────────── move() ────────────┘
 *                       │ (if win)
 *                       ▼
 *                   finished
 *
 * ─────────────────────────────────────────────────────────────────
 */

const TurnManager = (() => {
  let _state = null; /* GameState (private) */

  /* ─── Public API ─────────────────────────────────────────────── */

  /**
   * Initialises a new game.
   * @param {{ name: string, type: 'green'|'orange' }[]} playerConfigs - 1 to 4 entries
   * @returns {{ type: 'GAME_START', players: Player[], snapshot: object }}
   */
  function startGame(playerConfigs) {
    if (!Array.isArray(playerConfigs) || playerConfigs.length < 1 || playerConfigs.length > 4) {
      throw new Error('startGame: provide between 1 and 4 player configs.');
    }

    const players = playerConfigs.map((cfg, i) =>
      createPlayer(i + 1, cfg.name, cfg.type)
    );

    _state = createGameState(players);

    const event = { type: 'GAME_START', players: players.map(p => ({ ...p })) };
    _appendLog(event);
    return { ...event, snapshot: snapshotState(_state) };
  }

  /**
   * Rolls the dice for the current player.
   * Only valid when turnPhase === 'waiting_roll'.
   *
   * @param {number} [fixedValue]  - Optional override for testing (1–6)
   * @returns {{ type: 'ROLL', player: Player, diceValue: number, snapshot: object }}
   */
  function roll(fixedValue) {
    _guard('waiting_roll');

    const value = (fixedValue !== undefined)
      ? Dice.rollFixed(fixedValue)
      : Dice.roll();

    _state.diceValue  = value;
    _state.turnPhase  = 'waiting_move';

    const event = { type: 'ROLL', player: { ..._currentPlayer() }, diceValue: value };
    _appendLog(event);
    return { ...event, snapshot: snapshotState(_state) };
  }

  /**
   * Moves the current player by the previously rolled dice value.
   * Resolves snake/ladder effects, checks for win, then advances the turn.
   * Only valid when turnPhase === 'waiting_move'.
   *
   * Returned event shape:
   * {
   *   type:      'MOVE'
   *   player:    Player          — player who moved (pre-move snapshot)
   *   diceValue: number
   *   from:      number          — position before roll
   *   landed:    number          — position after dice (before effect)
   *   to:        number          — final position (after effect)
   *   effect:    'snake'|'ladder'|null
   *   isWin:     boolean
   *   snapshot:  object          — full state snapshot after move
   * }
   *
   * @returns {MoveEvent}
   */
  function move() {
    _guard('waiting_move');

    const playerIndex = _state.currentPlayerIndex;
    const player      = _state.players[playerIndex];
    const from        = player.position;
    const diceValue   = _state.diceValue;

    /* 1. Apply dice — with bounce-back if overshoot */
    const landed = Board.clampPosition(from, diceValue);

    /* 2. Resolve snake / ladder effect based on player type */
    const { finalPos: to, effectType: effect, direction } = Board.handleSpecialTiles(player, landed);

    /* 3. Commit new position */
    _state.players[playerIndex].position = to;

    /* 4. Check win */
    const isWin = Board.isWinPosition(to);

    const event = {
      type:      'MOVE',
      player:    { ...player },   /* snapshot of player before mutation */
      diceValue,
      from,
      landed,
      to,
      effect,      /* 'snake' | 'ladder' | null                       */
      direction,   /* 'up' | 'down' | null  — net movement of effect  */
      isWin,
    };
    _appendLog(event);

    /* 5. Resolve game phase */
    if (isWin) {
      _state.winner    = { ..._state.players[playerIndex] };
      _state.phase     = 'finished';
      const winEvent   = { type: 'WIN', player: { ..._state.winner } };
      _appendLog(winEvent);
    } else {
      _state.turnCount++;
      _state.currentPlayerIndex =
        (_state.currentPlayerIndex + 1) % _state.players.length;
    }

    /* 6. Reset turn phase */
    _state.diceValue = null;
    _state.turnPhase = 'waiting_roll';

    return { ...event, snapshot: snapshotState(_state) };
  }

  /**
   * Returns a safe snapshot of the current game state.
   * Returns null if the game has not been started.
   * @returns {object|null}
   */
  function getState() {
    return _state ? snapshotState(_state) : null;
  }

  /**
   * Returns a snapshot of the player whose turn it currently is.
   * @returns {Player|null}
   */
  function getCurrentPlayer() {
    return _state ? { ..._currentPlayer() } : null;
  }

  /**
   * Returns a copy of the full event log (for replays / debugging).
   * @returns {object[]}
   */
  function getLog() {
    return _state ? [..._state.log] : [];
  }

  /* ─── Private helpers ────────────────────────────────────────── */

  function _currentPlayer() {
    return _state.players[_state.currentPlayerIndex];
  }

  function _appendLog(event) {
    _state.log.push({ ...event, _ts: Date.now() });
  }

  /**
   * Asserts the game is running and in the expected turn phase.
   * Throws a descriptive error if either condition fails.
   * @param {'waiting_roll'|'waiting_move'} expectedPhase
   */
  function _guard(expectedPhase) {
    if (!_state) {
      throw new Error('Game not started. Call TurnManager.startGame() first.');
    }
    if (_state.phase === 'finished') {
      throw new Error(`Game is over. Winner: ${_state.winner?.name}. Call startGame() to restart.`);
    }
    if (_state.turnPhase !== expectedPhase) {
      throw new Error(
        `Action out of order — expected turnPhase "${expectedPhase}", ` +
        `but current phase is "${_state.turnPhase}".`
      );
    }
  }

  return Object.freeze({ startGame, roll, move, getState, getCurrentPlayer, getLog });
})();
