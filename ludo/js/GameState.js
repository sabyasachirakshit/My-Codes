/**
 * GameState.js
 * Factory for the mutable game state object.
 * Also provides a snapshot helper so callers always receive
 * plain data objects rather than live references.
 *
 * State shape:
 * {
 *   phase:               'playing' | 'finished'
 *   players:             Player[]          — ordered turn list
 *   currentPlayerIndex:  number            — index into players[]
 *   turnPhase:           'waiting_roll' | 'waiting_move'
 *   diceValue:           number | null     — null until current roll
 *   winner:              Player | null
 *   turnCount:           number            — increments after each full turn
 *   log:                 TurnEvent[]       — append-only event history
 * }
 */

/**
 * @param {Player[]} players  - Ordered array of 1–4 player objects
 * @returns {GameState}
 */
function createGameState(players) {
  if (!Array.isArray(players) || players.length < 1 || players.length > 4) {
    throw new Error(`createGameState: expected 1–4 players, got ${players?.length}`);
  }

  return {
    phase:               'playing',
    players:             players.map(p => ({ ...p })), /* shallow copy each player */
    currentPlayerIndex:  0,
    turnPhase:           'waiting_roll',
    diceValue:           null,
    winner:              null,
    turnCount:           0,
    log:                 [],
  };
}

/**
 * Returns a deep-enough snapshot of state safe to hand to the UI
 * (players array is cloned so callers can't accidentally mutate live state).
 * @param {GameState} state
 * @returns {object}
 */
function snapshotState(state) {
  return {
    phase:              state.phase,
    players:            state.players.map(p => ({ ...p })),
    currentPlayerIndex: state.currentPlayerIndex,
    turnPhase:          state.turnPhase,
    diceValue:          state.diceValue,
    winner:             state.winner ? { ...state.winner } : null,
    turnCount:          state.turnCount,
  };
}
