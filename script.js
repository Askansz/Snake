document.addEventListener('DOMContentLoaded', () => {
    const gameContainer = document.querySelector('.game-container');
    const snakeHead = document.getElementById('snake-head');
    const food = document.getElementById('food');
    const gameWidth = gameContainer.offsetWidth;
    const gameHeight = gameContainer.offsetHeight;
    const cellSize = 20;
    const maxCellX = gameWidth / cellSize;
    const maxCellY = gameHeight / cellSize;
    const directions = {
        'W': { x: 0, y: -1 },
        'S': { x: 0, y: 1 },
        'A': { x: -1, y: 0 },
        'D': { x: 1, y: 0 }
    };
    let currentDirection = directions['D'];
    let snakeX = 0;
    let snakeY = 0;
    let foodX;
    let foodY;
    let snakeTail = [];

    function getRandomPosition() {
        return Math.floor(Math.random() * maxCellX) * cellSize;
    }

    function updateSnake() {
        snakeX += currentDirection.x * cellSize;
        snakeY += currentDirection.y * cellSize;

        if (snakeX < 0 || snakeX >= gameWidth || snakeY < 0 || snakeY >= gameHeight) {
            gameOver();
        }

        snakeTail.unshift({ x: snakeX, y: snakeY });

        if (snakeX === foodX && snakeY === foodY) {
            createFood();
        } else {
            snakeTail.pop();
        }

        snakeHead.style.left = `${snakeX}px`;
        snakeHead.style.top = `${snakeY}px`;

        snakeTail.forEach((tailPart, index) => {
            const tailElement = document.getElementById(`tail-${index}`);
            tailElement.style.left = `${tailPart.x}px`;
            tailElement.style.top = `${tailPart.y}px`;

            if (tailPart.x === snakeX && tailPart.y === snakeY) {
                gameOver();
            }
        });
    }

    function createFood() {
        foodX = getRandomPosition();
        foodY = getRandomPosition();

        food.style.left = `${foodX}px`;
        food.style.top = `${foodY}px`;
    }

    function gameOver() {
        alert('Game Over');
        snakeX = 0;
        snakeY = 0;
        snakeTail = [];
        currentDirection = directions['D'];
        snakeHead.style.left = '0';
        snakeHead.style.top = '0';
        createFood();
    }

    function handleKeyDown(event) {
        const key = event.key.toUpperCase();

        if (key === 'W' && currentDirection !== directions['S']) {
            currentDirection = directions['W'];
        } else if (key === 'S' && currentDirection !== directions['W']) {
            currentDirection = directions['S'];
        } else if (key === 'A' && currentDirection !== directions['D']) {
            currentDirection = directions['A'];
        } else if (key === 'D' && currentDirection !== directions['A']) {
            currentDirection = directions['D'];
        }
    }

    createFood();
    setInterval(updateSnake, 200);
    document.addEventListener('keydown', handleKeyDown);
});
