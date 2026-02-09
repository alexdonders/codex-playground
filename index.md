---
layout: default
title: Home
---

<section class="intro">
  <p>Welcome to the sample Jekyll site. This homepage showcases how to structure a simple website using Jekyll.</p>
</section>

<section class="snake-game">
  <h2>Snake Game</h2>
  <p>Use the arrow keys (or WASD) to move. Press space to pause.</p>
  <div class="game-wrapper">
    <canvas id="snakeCanvas" width="400" height="400" aria-label="Snake game canvas"></canvas>
    <aside class="game-panel">
      <div><strong>Score:</strong> <span id="score">0</span></div>
      <div><strong>High Score:</strong> <span id="highScore">0</span></div>
      <button id="restartButton" type="button">Restart</button>
    </aside>
  </div>
</section>

<style>
  .snake-game {
    margin-top: 2rem;
  }

  .game-wrapper {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    align-items: flex-start;
  }

  #snakeCanvas {
    border: 2px solid #222;
    background: #f4f4f4;
  }

  .game-panel {
    display: grid;
    gap: 0.75rem;
    min-width: 160px;
  }

  .game-panel button {
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
  }
</style>

<script>
  (() => {
    const canvas = document.getElementById('snakeCanvas');
    const context = canvas.getContext('2d');
    const scoreEl = document.getElementById('score');
    const highScoreEl = document.getElementById('highScore');
    const restartButton = document.getElementById('restartButton');

    const gridSize = 20;
    const tileCount = canvas.width / gridSize;
    const baseSpeed = 120;

    let snake;
    let food;
    let direction;
    let pendingDirection;
    let score;
    let highScore = 0;
    let loopId;
    let paused = false;

    const randomPosition = () => ({
      x: Math.floor(Math.random() * tileCount),
      y: Math.floor(Math.random() * tileCount),
    });

    const resetGame = () => {
      snake = [
        { x: 10, y: 10 },
        { x: 9, y: 10 },
        { x: 8, y: 10 },
      ];
      direction = { x: 1, y: 0 };
      pendingDirection = direction;
      score = 0;
      scoreEl.textContent = score;
      food = randomPosition();
      paused = false;
    };

    const drawTile = (x, y, color) => {
      context.fillStyle = color;
      context.fillRect(x * gridSize, y * gridSize, gridSize, gridSize);
    };

    const draw = () => {
      context.clearRect(0, 0, canvas.width, canvas.height);
      drawTile(food.x, food.y, '#e74c3c');
      snake.forEach((segment, index) => {
        drawTile(segment.x, segment.y, index === 0 ? '#2c3e50' : '#3498db');
      });
    };

    const update = () => {
      if (paused) {
        return;
      }

      direction = pendingDirection;
      const head = {
        x: (snake[0].x + direction.x + tileCount) % tileCount,
        y: (snake[0].y + direction.y + tileCount) % tileCount,
      };

      if (snake.some(segment => segment.x === head.x && segment.y === head.y)) {
        resetGame();
        return;
      }

      snake.unshift(head);

      if (head.x === food.x && head.y === food.y) {
        score += 1;
        scoreEl.textContent = score;
        if (score > highScore) {
          highScore = score;
          highScoreEl.textContent = highScore;
        }
        do {
          food = randomPosition();
        } while (snake.some(segment => segment.x === food.x && segment.y === food.y));
      } else {
        snake.pop();
      }
    };

    const gameLoop = () => {
      update();
      draw();
    };

    const setDirection = (x, y) => {
      if (direction.x === -x && direction.y === -y) {
        return;
      }
      pendingDirection = { x, y };
    };

    const handleKeydown = event => {
      switch (event.key) {
        case 'ArrowUp':
        case 'w':
        case 'W':
          setDirection(0, -1);
          break;
        case 'ArrowDown':
        case 's':
        case 'S':
          setDirection(0, 1);
          break;
        case 'ArrowLeft':
        case 'a':
        case 'A':
          setDirection(-1, 0);
          break;
        case 'ArrowRight':
        case 'd':
        case 'D':
          setDirection(1, 0);
          break;
        case ' ':
          paused = !paused;
          break;
        default:
          break;
      }
    };

    const start = () => {
      resetGame();
      if (loopId) {
        clearInterval(loopId);
      }
      loopId = setInterval(gameLoop, baseSpeed);
    };

    document.addEventListener('keydown', handleKeydown);
    restartButton.addEventListener('click', start);

    start();
  })();
</script>
