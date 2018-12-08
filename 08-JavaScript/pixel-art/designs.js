
const colorPicker = document.getElementById('colorPicker');
const inputWidth = document.getElementById('inputWidth');
const inputHeight = document.getElementById('inputHeight');
const canvas = document.getElementById('pixelCanvas');

/**
 * @description Clears the contents of any existing grid
 */
function clearGrid() {
  canvas.innerHTML = '';
}

/**
 * @description Makes a grid of table cells corresponding
 * to the size specified in the form controls
 */
function makeGrid() {
  clearGrid();
  const width = Number(inputWidth.value);
  const height = Number(inputHeight.value);

  for (let rowIndex = 0; rowIndex < height; rowIndex++) {
    const newRow = document.createElement('tr');
    canvas.appendChild(newRow);
    for (let colIndex = 0; colIndex < width; colIndex++) {
      const newCol = document.createElement('td');
      newCol.addEventListener('click', onCellClick);
      newRow.appendChild(newCol);
    }
  }
}

/**
 * @description The event handler for the submit button click event.
 * @param {EventTarget} event - The EventTarget that contains information about the event.
 */
function onSubmit(event) {
  // The default action must be prevented so the form doesn't post back
  // and lose the html that is added in the makeGrid function.
  event.preventDefault();
  makeGrid();
}

/**
 * @description The event handler for the cell click event
 * @param {EventTarget} event - The EventTarget that contains information about the event.
 */
function onCellClick(event) {
  event.currentTarget.style.backgroundColor = colorPicker.value;
}

document.querySelector('input[type="submit"]').addEventListener('click', onSubmit);
