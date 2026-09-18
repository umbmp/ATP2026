while (notDone()) {
  if (isPathRight()) {
    turnRight();   // ↻
    moveForward(); // ↑
  } else {
    if (isPathForward()) {
      moveForward(); // ↑
    } else {
      turnLeft();    // ↺
    }
  }
}

//Link para o Blockly: Maze
//https://blockly.games/maze?lang=en&level=10&skin=0#twdgng