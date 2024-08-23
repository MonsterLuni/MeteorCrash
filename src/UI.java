import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.KeyEvent;
import java.time.Instant;
import java.util.ArrayList;

public class UI extends JPanel {
    GameManager gm;
    public UI(GameManager gm){
        this.gm = gm;
    }
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, getWidth(), getHeight());
        g.setColor(Color.red);
        g.drawLine(0,getHeight() - 50,getWidth(),getHeight() - 50);
        g.setFont(new Font("Arial",Font.BOLD,25));
        gm.currentPlayer.draw(g);
        for (int i = 0; i < gm.meteors.size(); i++){
            gm.meteors.get(i).draw(g);
        }
        for (int i = 0; i < gm.upgrades.size(); i++){
            gm.upgrades.get(i).draw(g);
        }
        g.setColor(Color.white);
        g.drawString(String.valueOf(gm.score),30,50);
        g.drawString(gm.currentPlayer.health + "/5",30,100);
    }
}

