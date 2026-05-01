/**
 * board-render.js
 * Responsible ONLY for rendering the board UI.
 * No game logic lives here.
 */

/* ─── Derive special-tile sets from shared CONFIG ───────────── */
const SNAKE_HEADS  = new Set(CONFIG.snakes.map(s => s.head));
const LADDER_BASES = new Set(CONFIG.ladders.map(l => l.base));

/* ─── Zig-zag tile number layout ─────────────────────────────── */
/**
 * Returns the tile number for a given grid position.
 * Grid is rendered top-to-bottom (row 0 = tile 91–100 visually at top).
 *
 * Layout (row index 0 = top of board):
 *   row 0 → tiles 91–100  (left to right → numbers increase left→right? No.)
 *
 * Standard S&L board numbering (bottom-left = 1):
 *   visual row 9 (bottom DOM row): 1  2  3  4  5  6  7  8  9  10
 *   visual row 8:                 20 19 18 17 16 15 14 13 12 11
 *   visual row 7:                 21 22 23 24 25 26 27 28 29 30
 *   ...
 *   visual row 0 (top DOM row):  100 99 98 97 96 95 94 93 92 91
 *
 * rowIndex 0 = bottom of visual board (tile 1)
 * We render DOM from top, so domRow = 9 - rowIndex
 */
function getTileNumber(domRow, col) {
  // domRow 0 = topmost in DOM = highest row visually
  const rowFromBottom = 9 - domRow; // 0 = bottom row (tiles 1-10)
  const rowBase = rowFromBottom * 10;

  if (rowFromBottom % 2 === 0) {
    // even rows from bottom → left to right: col 0 = lowest tile in row
    return rowBase + col + 1;
  } else {
    // odd rows from bottom → right to left: col 0 = highest tile in row
    return rowBase + (9 - col) + 1;
  }
}

/* ─── Build the board ─────────────────────────────────────────── */
function renderBoard() {
  const board = document.getElementById('board');
  const fragment = document.createDocumentFragment();

  for (let domRow = 0; domRow < 10; domRow++) {
    for (let col = 0; col < 10; col++) {
      const tileNum = getTileNumber(domRow, col);

      const tile = document.createElement('div');
      tile.classList.add('tile');
      tile.dataset.tile = tileNum;

      /* Snake / ladder placeholder classes */
      if (SNAKE_HEADS.has(tileNum))  tile.classList.add('has-snake');
      if (LADDER_BASES.has(tileNum)) tile.classList.add('has-ladder');

      /* Row-start direction arrow (zig-zag visual cue) */
      const rowFromBottom = 9 - domRow;
      if (col === 0) {
        tile.classList.add('row-start');
        tile.dataset.arrow = rowFromBottom % 2 === 0 ? '→' : '←';
      }

      /* Number label */
      const label = document.createElement('span');
      label.classList.add('tile-number');
      label.textContent = tileNum;

      /* Empty token slot container (players placed here later) */
      const tokens = document.createElement('div');
      tokens.classList.add('tile-tokens');

      tile.appendChild(tokens);
      tile.appendChild(label);
      fragment.appendChild(tile);
    }
  }

  board.appendChild(fragment);
}

/* ─── Legend HTML ─────────────────────────────────────────────── */
function renderLegend() {
  const gameArea = document.querySelector('.game-area');

  const legend = document.createElement('div');
  legend.classList.add('legend');
  legend.innerHTML = `
    <div class="legend-item"><div class="legend-swatch start"></div> Start (1)</div>
    <div class="legend-item"><div class="legend-swatch goal"></div> Goal (100)</div>
    <div class="legend-item"><div class="legend-swatch snake"></div> 🐍 Snake head</div>
    <div class="legend-item"><div class="legend-swatch ladder"></div> 🪜 Ladder base</div>
  `;

  const typeLegend = document.createElement('div');
  typeLegend.classList.add('player-type-legend');
  typeLegend.innerHTML = `
    <div class="type-item">
      <div class="type-dot green"></div>
      <div class="type-label">
        <strong>Green player</strong>
        <span>Climbs ladders · slides snakes</span>
      </div>
    </div>
    <div class="type-item">
      <div class="type-dot orange"></div>
      <div class="type-label">
        <strong>Orange player</strong>
        <span>Climbs snakes · slides ladders</span>
      </div>
    </div>
  `;

  gameArea.appendChild(legend);
  gameArea.appendChild(typeLegend);
}

/* ─── Init ────────────────────────────────────────────────────── */
renderBoard();
renderLegend();
