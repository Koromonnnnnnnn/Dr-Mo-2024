import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimplePong extends JPanel implements ActionListener, KeyListener {
    int ballX = 150, ballY = 100, ballDX = 1, ballDY = 1;
    int paddleX = 150, paddleY = 250;
    Timer timer = new Timer(5, this);

    public SimplePong() {
        JFrame frame = new JFrame("Simple Pong");
        frame.setSize(300, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.addKeyListener(this);
        frame.setVisible(true);
        timer.start();
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.fillRect(ballX, ballY, 10, 10); // Draw the ball
        g.fillRect(paddleX, paddleY, 60, 10); // Draw the paddle
    }

    public void actionPerformed(ActionEvent e) {
        ballX += ballDX;
        ballY += ballDY;
        if (ballX < 0 || ballX > getWidth() - 10) ballDX *= -1; // Bounce ball off walls
        if (ballY < 0 || ballY > getHeight() - 10) ballDY *= -1; // Bounce ball off top/bottom
        if (ballY > paddleY - 10 && ballX + 10 > paddleX && ballX < paddleX + 60) ballDY *= -1; // Bounce ball off paddle
        repaint();
    }

    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_LEFT && paddleX > 0) paddleX -= 10; // Move paddle left
        if (e.getKeyCode() == KeyEvent.VK_RIGHT && paddleX < getWidth() - 60) paddleX += 10; // Move paddle right
    }

    public void keyReleased(KeyEvent e) {}
    public void keyTyped(KeyEvent e) {}

    public static void main(String[] args) {
        SwingUtilities.invokeLater(SimplePong::new);
    }
}
