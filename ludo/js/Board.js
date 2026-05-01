/**
 * Board.js
 * Core board logic: position clamping and snake/ladder effect resolution.
 * Depends on CONFIG (config.js) being loaded first.
 *
 * ─── handleSpecialTiles logic ────────────────────────────────────
 *
 *  Every snake and ladder has two endpoints (high tile, low tile).
 *  Which endpoint acts as the ENTRY depends entirely on player type:
 *
 *  Player type │ Lands on…      │ Teleports to… │ Net movement
 *  ────────────┼────────────────┼───────────────┼─────────────
 *  green       │ ladder BASE    │ ladder TOP    │ ⬆ up   (reward)
 *  green       │ snake HEAD     │ snake TAIL    │ ⬇ down (penalty)
 *  orange      │ snake TAIL     │ snake HEAD    │ ⬆ up   (reward — climbs snake)
 *  orange      │ ladder TOP     │ ladder BASE   │ ⬇ down (penalty — slides ladder)
 *  any         │ any other tile │ same tile     │ — no effect
 *  ────────────┴────────────────┴───────────────┴─────────────
 *
 *  Orange is the full inverse: what hurts Green helps Orange and vice versa.
 *  The entry tile differs (HEAD vs TAIL for snakes, BASE vs TOP for ladders),
 *  so landing on the wrong end of a snake/ladder does nothing for either type.
 *
 * Maps are built once at load time from CONFIG for O(1) lookup.
 */

const Board = (() => {
  /* ─── Build O(1) lookup maps from CONFIG ──────────────────── */
  /* green-entry maps */
  const snakeByHead   = new Map(CONFIG.snakes.map(s  => [s.head,  s.tail]));
  const ladderByBase  = new Map(CONFIG.ladders.map(l => [l.base,  l.top]));

  /* orange-entry maps (inverted endpoints) */
  const snakeByTail   = new Map(CONFIG.snakes.map(s  => [s.tail,  s.head]));
  const ladderByTop   = new Map(CONFIG.ladders.map(l => [l.top,   l.base]));

  /* ─── Position clamping ────────────────────────────────────── */
  /**
   * Moves a player from `current` by `diceValue` steps.
   * If the result overshoots CONFIG.boardSize, the player bounces back.
   *
   *   Example: position 97, roll 5 → raw 102 → bounce → 100 - (102 - 100) = 98
   *
   * @param {number} current
   * @param {number} diceValue
   * @returns {number}
   */
  function clampPosition(current, diceValue) {
    const raw = current + diceValue;
    if (raw > CONFIG.boardSize) {
      return CONFIG.boardSize - (raw - CONFIG.boardSize); /* bounce-back */
    }
    return raw;
  }

  /* ─── Internal: resolve by type string ───────────────────────── */
  /**
   * Core lookup — kept private so callers always go through
   * handleSpecialTiles() and pass a full player object.
   *
   * @param {number} position
   * @param {'green'|'orange'} type
   * @returns {{ finalPos: number, effectType: 'snake'|'ladder'|null }}
   */
  function _resolveByType(position, type) {
    if (type === 'green') {
      /* Green entry points: ladder BASE (go up), snake HEAD (go down) */
      if (ladderByBase.has(position)) return { finalPos: ladderByBase.get(position), effectType: 'ladder' };
      if (snakeByHead.has(position))  return { finalPos: snakeByHead.get(position),  effectType: 'snake'  };
    } else {
      /* Orange entry points: snake TAIL (go up), ladder TOP (go down) */
      if (snakeByTail.has(position))  return { finalPos: snakeByTail.get(position),  effectType: 'snake'  };
      if (ladderByTop.has(position))  return { finalPos: ladderByTop.get(position),  effectType: 'ladder' };
    }
    return { finalPos: position, effectType: null };
  }

  /* ─── Public: handleSpecialTiles ──────────────────────────────── */
  /**
   * Given a player object and the tile they just landed on, returns
   * where they actually end up after any snake or ladder is applied.
   *
   * This is the single, reusable function the rest of the engine calls
   * for all special-tile resolution. It is type-aware: the same tile
   * number can be an entry for Green but a no-op for Orange, and vice versa.
   *
   * How it works (step by step):
   *   1. Read player.type ('green' or 'orange').
   *   2. For GREEN  — check if position is a ladder base (teleport up)
   *                   then check if position is a snake head (teleport down).
   *   3. For ORANGE — check if position is a snake tail  (teleport up)
   *                   then check if position is a ladder top (teleport down).
   *   4. If no match — return position unchanged (effectType: null).
   *
   * @param {{ type: 'green'|'orange' }} player  - Player object (only .type is read)
   * @param {number}                    position - Tile the player landed on
   * @returns {{
   *   finalPos:   number,                    The tile the player ends up on
   *   effectType: 'snake'|'ladder'|null,     What triggered (null = nothing)
   *   direction:  'up'|'down'|null           Net movement direction
   * }}
   */
  function handleSpecialTiles(player, position) {
    const { finalPos, effectType } = _resolveByType(position, player.type);
    const direction = effectType === null
      ? null
      : finalPos > position ? 'up' : 'down';

    return { finalPos, effectType, direction };
  }

  /* ─── Win check ────────────────────────────────────────────── */
  /**
   * @param {number} position
   * @returns {boolean}
   */
  function isWinPosition(position) {
    return position === CONFIG.boardSize;
  }

  /* ─── Debug helper ─────────────────────────────────────────── */
  /**
   * Returns a human-readable description of a tile's effect for
   * a given player type. Used for logging and testing.
   * @param {number} position
   * @param {'green'|'orange'} playerType
   * @returns {string}
   */
  function describeEffect(position, playerType) {
    const mockPlayer = { type: playerType };
    const { finalPos, effectType, direction } = handleSpecialTiles(mockPlayer, position);
    if (!effectType) return `Tile ${position}: no effect (${playerType})`;
    const arrow = direction === 'up' ? '⬆' : '⬇';
    return `Tile ${position}: ${effectType} ${arrow} ${direction} → ${finalPos} (${playerType})`;
  }

  return Object.freeze({ clampPosition, handleSpecialTiles, isWinPosition, describeEffect });
})();
