/**
 * overlay-render.js
 * Draws an SVG layer of snakes and ladders over the tile grid.
 * Pure rendering — reads CONFIG, measures real DOM positions.
 * No game logic lives here.
 *
 * ─── Coordinate System ───────────────────────────────────────────
 *
 * The SVG uses viewBox="0 0 100 100" placed absolutely over the board.
 * Every tile number maps to an (x, y) in that 0–100 space like this:
 *
 *   1. Look up the tile's DOM element via data-tile attribute.
 *   2. Call getBoundingClientRect() to get its real pixel position.
 *   3. Subtract the SVG's own origin (= board content-area top-left,
 *      which sits INSIDE the board's 3 px border — hence we subtract
 *      board.clientLeft / clientTop from the boardRect origin).
 *   4. Divide by the SVG's pixel dimensions → fraction 0–1.
 *   5. Multiply by 100 → SVG user units.
 *
 *   x = ((tile.cx_px  − svgOriginX) / svgWidthPx)  × 100
 *   y = ((tile.cy_px  − svgOriginY) / svgHeightPx) × 100
 *
 * This is fully gap-agnostic: border widths, grid gap, responsive
 * scaling — none of it needs manual accounting.
 * ─────────────────────────────────────────────────────────────────
 */

const SNAKE_PALETTE  = ['#e53935', '#d81b60', '#7b1fa2', '#e65100', '#00838f'];
const LADDER_PALETTE = ['#f9a825', '#2e7d32', '#1565c0', '#6a1b9a', '#00695c', '#bf360c'];

/* ─── SVG element factory ───────────────────────────────────── */
function svgEl(tag, attrs = {}) {
  const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, v);
  return el;
}

/* ─── Tile → SVG coordinate ─────────────────────────────────── */
function tileCoords(tileNum, board) {
  const tile = document.querySelector(`[data-tile="${tileNum}"]`);
  if (!tile) return { x: 0, y: 0 };

  const tr = tile.getBoundingClientRect();
  const br = board.getBoundingClientRect();

  /* board.clientLeft/Top = actual border-width pixels (usually 3px here) */
  const ox = br.left + board.clientLeft;
  const oy = br.top  + board.clientTop;
  const sw = board.clientWidth;
  const sh = board.clientHeight;

  return {
    x: ((tr.left + tr.width  / 2) - ox) / sw * 100,
    y: ((tr.top  + tr.height / 2) - oy) / sh * 100,
  };
}

/* ─── Ladder ────────────────────────────────────────────────── */
function drawLadder(group, defs, ladder, idx, board) {
  const { x: x1, y: y1 } = tileCoords(ladder.base, board);
  const { x: x2, y: y2 } = tileCoords(ladder.top,  board);

  const dx = x2 - x1, dy = y2 - y1;
  const len = Math.hypot(dx, dy);
  if (len === 0) return;

  const ux = dx / len, uy = dy / len;   /* unit direction  */
  const px = -uy,      py =  ux;        /* unit perpendicular */
  const rail   = 1.1;                   /* half-width of rail pair  */
  const color  = LADDER_PALETTE[idx % LADDER_PALETTE.length];
  const nRungs = Math.max(2, Math.round(len / 9));

  const g = svgEl('g', { class: 'ladder', opacity: '0.9' });

  /* Two rails */
  for (const s of [1, -1]) {
    g.appendChild(svgEl('line', {
      x1: x1 + px * rail * s, y1: y1 + py * rail * s,
      x2: x2 + px * rail * s, y2: y2 + py * rail * s,
      stroke: color, 'stroke-width': '1.3', 'stroke-linecap': 'round',
    }));
  }

  /* Rungs */
  for (let i = 1; i <= nRungs; i++) {
    const t  = i / (nRungs + 1);
    const rx = x1 + ux * len * t;
    const ry = y1 + uy * len * t;
    g.appendChild(svgEl('line', {
      x1: rx + px * rail, y1: ry + py * rail,
      x2: rx - px * rail, y2: ry - py * rail,
      stroke: color, 'stroke-width': '0.9', 'stroke-linecap': 'round',
    }));
  }

  /* Base marker */
  g.appendChild(svgEl('circle', { cx: x1, cy: y1, r: '1.7', fill: color }));

  /* Top cap (open circle) */
  g.appendChild(svgEl('circle', {
    cx: x2, cy: y2, r: '1.3',
    fill: '#fff', stroke: color, 'stroke-width': '0.8',
  }));

  group.appendChild(g);
}

/* ─── Snake ─────────────────────────────────────────────────── */
function drawSnake(group, defs, snake, idx, board) {
  const { x: hx, y: hy } = tileCoords(snake.head, board); /* head = high tile */
  const { x: tx, y: ty } = tileCoords(snake.tail, board); /* tail = low  tile */

  const dx = tx - hx, dy = ty - hy;
  const len = Math.hypot(dx, dy);
  if (len === 0) return;

  const px = -dy / len, py = dx / len;   /* perpendicular */
  const c  = len * 0.28;                 /* curviness     */

  /* Cubic bezier — S-curve with perpendicular control points */
  const cp1x = hx + dx * 0.33 + px * c, cp1y = hy + dy * 0.33 + py * c;
  const cp2x = hx + dx * 0.67 - px * c, cp2y = hy + dy * 0.67 - py * c;

  const color = SNAKE_PALETTE[idx % SNAKE_PALETTE.length];
  const gid   = `sg${idx}`;

  /* Body gradient: head color → dark green at tail */
  const grad = svgEl('linearGradient', {
    id: gid, gradientUnits: 'userSpaceOnUse',
    x1: hx, y1: hy, x2: tx, y2: ty,
  });
  grad.appendChild(svgEl('stop', { offset: '0%',   'stop-color': color }));
  grad.appendChild(svgEl('stop', { offset: '100%', 'stop-color': '#1b5e20' }));
  defs.appendChild(grad);

  const g = svgEl('g', { class: 'snake' });

  /* Body */
  g.appendChild(svgEl('path', {
    d: `M ${hx} ${hy} C ${cp1x} ${cp1y} ${cp2x} ${cp2y} ${tx} ${ty}`,
    stroke: `url(#${gid})`, 'stroke-width': '2.0',
    'stroke-linecap': 'round', fill: 'none', opacity: '0.9',
  }));

  /* Head disc */
  g.appendChild(svgEl('circle', { cx: hx, cy: hy, r: '2.1', fill: color }));

  /* Facing angle — direction from cp2 toward head */
  const ang = Math.atan2(hy - cp2y, hx - cp2x);
  const ca = Math.cos(ang), sa = Math.sin(ang);
  const ep = { x: -sa, y: ca }; /* eye perpendicular */

  /* Eyes */
  for (const s of [1, -1]) {
    const ex = hx + ca * 0.8 + ep.x * 0.75 * s;
    const ey = hy + sa * 0.8 + ep.y * 0.75 * s;
    g.appendChild(svgEl('circle', { cx: ex, cy: ey, r: '0.55', fill: '#fff' }));
    g.appendChild(svgEl('circle', { cx: ex + ca * 0.15, cy: ey + sa * 0.15, r: '0.25', fill: '#111' }));
  }

  /* Forked tongue */
  const ts = { x: hx + ca * 2.1, y: hy + sa * 2.1 }; /* tongue stem start */
  const tm = { x: hx + ca * 3.5, y: hy + sa * 3.5 }; /* fork split point  */
  const fork = 0.8;
  const f1 = { x: tm.x + ca * fork - sa * fork, y: tm.y + sa * fork + ca * fork };
  const f2 = { x: tm.x + ca * fork + sa * fork, y: tm.y + sa * fork - ca * fork };

  const tongueAttrs = { stroke: '#ff5252', 'stroke-width': '0.45', fill: 'none', 'stroke-linecap': 'round' };
  g.appendChild(svgEl('polyline', { points: `${ts.x},${ts.y} ${tm.x},${tm.y} ${f1.x},${f1.y}`, ...tongueAttrs }));
  g.appendChild(svgEl('polyline', { points: `${tm.x},${tm.y} ${f2.x},${f2.y}`,                 ...tongueAttrs }));

  /* Tail tip */
  g.appendChild(svgEl('circle', { cx: tx, cy: ty, r: '1.0', fill: '#1b5e20' }));

  group.appendChild(g);
}

/* ─── Main render ────────────────────────────────────────────── */
function renderOverlay() {
  const board    = document.getElementById('board');
  const existing = document.getElementById('board-overlay');
  if (existing) existing.remove();

  const svg  = svgEl('svg', {
    id: 'board-overlay',
    viewBox: '0 0 100 100',
    preserveAspectRatio: 'none',
    xmlns: 'http://www.w3.org/2000/svg',
  });

  const defs     = svgEl('defs');
  const ladderGrp = svgEl('g', { class: 'ladders-layer' });
  const snakeGrp  = svgEl('g', { class: 'snakes-layer' });

  svg.appendChild(defs);

  CONFIG.ladders.forEach((l, i) => drawLadder(ladderGrp, defs, l, i, board));
  CONFIG.snakes.forEach( (s, i) => drawSnake(snakeGrp,  defs, s, i, board));

  svg.appendChild(ladderGrp);  /* ladders drawn first (below snakes) */
  svg.appendChild(snakeGrp);

  board.appendChild(svg);
}

/* ─── Debounced resize ───────────────────────────────────────── */
let _resizeTimer;
window.addEventListener('load',   renderOverlay);
window.addEventListener('resize', () => {
  clearTimeout(_resizeTimer);
  _resizeTimer = setTimeout(renderOverlay, 120);
});
