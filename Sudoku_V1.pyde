int table[][] = new int[4][4];

void setup() {
  size(1000, 1000);
  background(255);
  
  generateSudoku();
  makePuzzle(8);
  drawGrid();
}

void drawGrid() {
  int cell = width / 4;
  

  for (int i = 0; i <= 4; i++) {
    if (i == 0 || i == 4) {
      strokeWeight(6);
    } else if (i % 2 == 0) {
      strokeWeight(3);
    } else {
      strokeWeight(1);  
    }
    line(i*cell, 0, i*cell, height);
    line(0, i*cell, width, i*cell);
  }
  
  textAlign(CENTER, CENTER);
  textSize(200);
  fill(0);
  for (int r = 0; r < 4; r++) {
    for (int c = 0; c < 4; c++) {
      if (table[r][c] != 0) {
        text(table[r][c], c*cell + cell/2, r*cell + cell/2);
      }
    }
  }
}

void generateSudoku() {
  solve(0, 0);
}

boolean solve(int row, int col) {
  if (row == 4) {
    return true;
  }

  int nextRow;
  int nextCol;
  if (col == 3) {
    nextRow = row + 1;
    nextCol = 0;
  } else {
    nextRow = row;
    nextCol = col + 1;
  }

  int[] nums = {1,2,3,4};
  shuffle(nums);

  for (int n : nums) {
    if (isSafe(row, col, n)) {
      table[row][col] = n;
      if (solve(nextRow, nextCol)) {
        return true;
      }
      table[row][col] = 0;
    }
  }
  return false;
}

boolean isSafe(int row, int col, int n) {
  for (int c = 0; c < 4; c++) {
    if (table[row][c] == n) {
      return false;
    }
  }
  for (int r = 0; r < 4; r++) {
    if (table[r][col] == n) {
      return false;
    }
  }
  int startRow = (row/2) * 2;
  int startCol = (col/2) * 2;
  for (int r = startRow; r < startRow+2; r++) {
    for (int c = startCol; c < startCol+2; c++) {
      if (table[r][c] == n) {
        return false;
      }
    }
  }
  return true;
}

void shuffle(int[] arr) {
  for (int i = arr.length-1; i > 0; i--) {
    int j = int(random(i+1));
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
}

void makePuzzle(int emptyCount) {
  int removed = 0;
  while (removed < emptyCount) {
    int r = int(random(4));
    int c = int(random(4));
    if (table[r][c] != 0) {
      table[r][c] = 0;
      removed++;
    }
  }
}
