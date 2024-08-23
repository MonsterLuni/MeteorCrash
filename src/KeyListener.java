import java.awt.event.KeyEvent;

public class KeyListener implements java.awt.event.KeyListener {
    GameManager gm;
    public boolean wPressed,aPressed,sPressed,dPressed;
    public KeyListener(GameManager gm){
        this.gm = gm;
    }

    @Override
    public void keyTyped(KeyEvent e) {}

    @Override
    public void keyPressed(KeyEvent e) {
        System.out.println("Gedrückt");
        switch (e.getKeyCode()) {
            case KeyEvent.VK_W -> wPressed = true;
            case KeyEvent.VK_A -> aPressed = true;
            case KeyEvent.VK_S -> sPressed = true;
            case KeyEvent.VK_D -> dPressed = true;
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
        switch (e.getKeyCode()) {
            case KeyEvent.VK_W -> wPressed = false;
            case KeyEvent.VK_A -> aPressed = false;
            case KeyEvent.VK_S -> sPressed = false;
            case KeyEvent.VK_D -> dPressed = false;
        }
    }
}
