using static System.Console;

namespace Program
{
    public class Program
    {
        public enum Direction
        {
            Up,
            Down,
            Left,
            Right,
        }

        public static int Score { get; set; } = 3;

        public static int WindowWidth { get; set; } = 32;
        public static int WindowHeight { get; set; } = 16;
        public static bool GameOver { get; private set; } = false;

        private static readonly Random rnd = new Random();
        private static readonly List<Pixel> SnakeBody = new List<Pixel>();
        private static readonly Pixel SnakeHead = new Pixel(10, 10, ConsoleColor.White);

        private static void Main(string[] args)
        {
            CursorVisible = false;
            SnakeBody.Add(new Pixel(SnakeHead.XPos - 1, SnakeHead.YPos, ConsoleColor.White));
            SnakeBody.Add(new Pixel(SnakeHead.XPos - 2, SnakeHead.YPos, ConsoleColor.White));

            int berryX = rnd.Next(0, WindowWidth - 2);
            int berryY = rnd.Next(0, WindowHeight - 2);
            var berryLocation = new Pixel(berryX, berryY, ConsoleColor.Yellow);
            DrawPixel(berryLocation);
            Direction direction = Direction.Right;

            while (!GameOver)
            {
                ClearLines();
                DrawBorder();
                DrawPixel(berryLocation);
                MoveSnake(direction);
                DrawPixel(SnakeHead);
                foreach (Pixel pxl in SnakeBody)
                {
                    DrawPixel(pxl);
                    if ((SnakeHead.XPos == pxl.XPos && SnakeHead.YPos == pxl.YPos))
                    {
                        GameOver = true;
                    }
                }

                if (SnakeHead.XPos == berryLocation.XPos && SnakeHead.YPos == berryLocation.YPos)
                {
                    Score++;
                    berryX = rnd.Next(1, WindowWidth - 1);
                    berryY = rnd.Next(1, WindowHeight - 1);
                    berryLocation = new Pixel(berryX, berryY, ConsoleColor.Yellow);
                    AddToSnake(direction);
                    DrawPixel(berryLocation);
                }
                if (KeyAvailable)
                {
                    direction = ChangeDirection(ReadKey(true), direction);
                }
                Thread.Sleep(50);
            }
            if (GameOver)
            {
                Clear();
                SetCursorPosition(WindowHeight / 5, WindowWidth / 5);
                WriteLine("GAME OVER \n\r Score: {0}", Score-3);
            }
        }

        private static void ClearLines()
        {
            for (int i = 0; i <= WindowHeight - 1; i++)
            {
                SetCursorPosition(0, i);
                Write(new String(' ', WindowWidth));
            }
        }

        private static void AddToSnake(Direction direction)
        {
            int x = SnakeBody.Last().XPos;
            int y = SnakeBody.Last().YPos;
            switch (direction)
            {
                case Direction.Up:
                    SnakeBody.Add(new Pixel(x, y - 1, ConsoleColor.White));
                    break;

                case Direction.Down:
                    SnakeBody.Add(new Pixel(x, y + 1, ConsoleColor.White));
                    break;

                case Direction.Left:
                    SnakeBody.Add(new Pixel(x - 1, y, ConsoleColor.White));
                    break;

                case Direction.Right:
                    SnakeBody.Add(new Pixel(x + 1, y, ConsoleColor.White));
                    break;
            }
        }

        private static void MoveSnake(Direction direction)
        {
            SnakeBody.Add(new Pixel(SnakeHead.XPos, SnakeHead.YPos, ConsoleColor.Green));
            switch (direction)
            {
                case Direction.Up:
                    if (SnakeHead.YPos == 1)
                    {
                        SnakeHead.YPos = WindowHeight - 1;
                    }
                    else
                    {
                        SnakeHead.YPos -= 1;
                    }
                    break;

                case Direction.Down:
                    if (SnakeHead.YPos == WindowHeight - 1)
                    {
                        SnakeHead.YPos = 1;
                    }
                    else
                    {
                        SnakeHead.YPos += 1;
                    }
                    break;

                case Direction.Left:
                    if (SnakeHead.XPos == 1)
                    {
                        SnakeHead.XPos = WindowWidth - 1;
                    }
                    else
                    {
                        SnakeHead.XPos -= 1;
                    }
                    break;

                case Direction.Right:
                    if (SnakeHead.XPos == WindowWidth - 1)
                    {
                        SnakeHead.XPos = 1;
                    }
                    else
                    {
                        SnakeHead.XPos += 1;
                    }
                    break;
            }
            if (SnakeBody.Count > Score)
            {
                SnakeBody.RemoveAt(0);
            }
        }

        private static Direction ChangeDirection(ConsoleKeyInfo consoleKeyInfo, Direction direction)
        {
            if (consoleKeyInfo.Key == ConsoleKey.UpArrow && direction != Direction.Down)
                return Direction.Up;
            if (consoleKeyInfo.Key == ConsoleKey.DownArrow && direction != Direction.Up)
                return Direction.Down;
            if (consoleKeyInfo.Key == ConsoleKey.LeftArrow && direction != Direction.Right)
                return Direction.Left;
            if (consoleKeyInfo.Key == ConsoleKey.RightArrow && direction != Direction.Left)
                return Direction.Right;
            return direction;
        }

        private static void DrawBorder()
        {
            for (int i = 0; i < WindowWidth; i++)
            {
                SetCursorPosition(i, 0);
                Write("■");

                SetCursorPosition(i, WindowHeight);
                Write("■");
            }

            for (int i = 0; i < WindowHeight; i++)
            {
                SetCursorPosition(0, i);
                Write("■");

                SetCursorPosition(WindowWidth, i);
                Write("■");
            }
        }

        private static void DrawPixel(Pixel pixel)
        {
            try
            {
                SetCursorPosition(pixel.XPos, pixel.YPos);
            }
            catch (ArgumentOutOfRangeException e)
            {
                GameOver = true;
            }
            ForegroundColor = pixel.ScreenColor;
            Write("■");
        }
    }

    internal class Pixel
    {
        public Pixel(int xPos, int yPos, ConsoleColor color)
        {
            XPos = xPos;
            YPos = yPos;
            ScreenColor = color;
        }

        public int XPos { get; set; }
        public int YPos { get; set; }
        public ConsoleColor ScreenColor { get; set; }
    }
}