/**
 * Player.js
 * Factory for player objects. No DOM, no state mutation here.
 *
 * Player types:
 *   'green'  — normal:   climbs ladders, slides down snakes
 *   'orange' — inverted: climbs snakes,  slides down ladders
 */

const VALID_TYPES = ['green', 'orange'];

/**
 * @param {number} id    - Unique player ID (1–4)
 * @param {string} name  - Display name
 * @param {string} type  - 'green' | 'orange'
 * @returns {Player}
 */
function createPlayer(id, name, type) {
  if (!VALID_TYPES.includes(type)) {
    throw new Error(`Invalid player type "${type}". Must be one of: ${VALID_TYPES.join(', ')}`);
  }
  if (id < 1 || id > 4) {
    throw new Error(`Player id must be 1–4, got ${id}`);
  }

  return {
    id,
    name,
    type,       /* 'green' | 'orange' */
    position: 0, /* 0 = off-board start; 1–100 = in play; 100 = win */
  };
}
