int table[][] = {
  {1,2,3,4},
  {1,2,3,4},
  {1,2,3,4},
  {1,2,3,4}
};

void setup() {
  size(1000,1000);
  background(255);
  drawGrid();
}

void drawGrid() {
  int cell = width / 4;
  
  for (int i = 0; i <= 4; i++) {
    if (i % 2 == 0) {
      strokeWeight(4);  
    } else {
      strokeWeight(1); 
    }
    line(i*cell, 0, i*cell, height);

    if (i % 2 == 0) {
      strokeWeight(4);
    } else {
      strokeWeight(1);
    }
    line(0, i*cell, width, i*cell);
  }
  
  textAlign(CENTER, CENTER);
  textSize(32);
  fill(0);
  for (int r = 0; r < 4; r++) {
    for (int c = 0; c < 4; c++) {
      text(table[r][c], c*cell + cell/2, r*cell + cell/2);
    }
  }
}
