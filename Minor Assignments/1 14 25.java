import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimplePong extends JPanel implements ActionListener, KeyListener {
    int ballX = 350, ballY = 250, ballDX = 1, ballDY = 1;
    int paddleX = 20, paddleY = 200;
    int paddle2X = 650, paddle2Y = 200;
    Timer timer = new Timer(5, this);

    public SimplePong() {
        JFrame frame = new JFrame("Simple Pong");
        frame.setSize(700, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.addKeyListener(this);
        frame.setVisible(true);
        timer.start();
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.fillRect(ballX, ballY, 25, 25); // Draw the ball
        g.fillRect(paddleX, paddleY, 10, 90); // Draw the paddle
        g.fillRect(paddle2X, paddle2Y, 10, 90); // Draw the paddle
    }

    public void actionPerformed(ActionEvent e) {
        ballX += ballDX;
        ballY += ballDY;
        if (ballX < 0 || ballX > getWidth() - 10) ballDX *= -1; // Bounce ball off walls
        if (ballY < 0 || ballY > getHeight() - 10) ballDY *= -1; // Bounce ball off top/bottom
        if (ballX - 20 < paddleX + 20 && ballY + 20 > paddleY && ballY < paddleY + 100) ballDX *= -1;
        if (ballY < paddle2Y + 100 && ballX + 20 > paddle2X && ballY + 20 > paddle2Y) ballDX *= -1;
        repaint();
    }

    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_UP && paddleY > 0) paddleY -= 10; // Move paddle left
        if (e.getKeyCode() == KeyEvent.VK_DOWN && paddleY < getWidth() - 60) paddleY += 10; // Move paddle right
        if (e.getKeyCode() == KeyEvent.VK_W && paddle2Y > 0) paddle2Y -= 10; // Move paddle left
        if (e.getKeyCode() == KeyEvent.VK_S && paddle2Y < getWidth() - 60) paddle2Y += 10; // Move paddle right
    }

    public void keyReleased(KeyEvent e) {}
    public void keyTyped(KeyEvent e) {}

    public static void main(String[] args) {
        SwingUtilities.invokeLater(SimplePong::new);
    }
}
