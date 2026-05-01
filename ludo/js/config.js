/**
 * config.js
 * Single source of truth for board topology.
 * Both the tile renderer and SVG overlay consume this.
 *
 * Snakes  — head: high tile (entry), tail: low tile (exit for Green)
 * Ladders — base: low tile  (entry), top:  high tile (exit for Green)
 */
const CONFIG = {
  boardSize: 100,

  snakes: [
    { head: 99, tail: 21 },
    { head: 54, tail: 34 },
    { head: 40, tail:  3 },
    { head: 27, tail:  5 },
    { head: 73, tail: 44 },
  ],

  ladders: [
    { base:  4, top: 14 },
    { base: 13, top: 46 },
    { base: 33, top: 58 },
    { base: 42, top: 63 },
    { base: 50, top: 91 },
    { base:  7, top: 48 },
  ],
};
