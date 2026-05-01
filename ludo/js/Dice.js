/**
 * Dice.js
 * Pure dice-roll logic. No state, no side effects.
 */

const Dice = (() => {
  const FACES = 6;

  /**
   * Returns a uniformly random integer in [1, FACES].
   * @returns {number}
   */
  function roll() {
    return Math.floor(Math.random() * FACES) + 1;
  }

  /**
   * Deterministic roll used in tests — pass an override value.
   * Validates the value is a legal face before returning it.
   * @param {number} value
   * @returns {number}
   */
  function rollFixed(value) {
    if (!Number.isInteger(value) || value < 1 || value > FACES) {
      throw new Error(`rollFixed: value must be an integer in [1, ${FACES}], got ${value}`);
    }
    return value;
  }

  return Object.freeze({ roll, rollFixed, FACES });
})();
