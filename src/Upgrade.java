import java.awt.*;
import java.util.Random;

public class Upgrade {
    Point coordinates;
    int size = 20;
    String stat;
    Color color;
    GameManager gm;
    int i = 0;
    public Upgrade(Color color,String stat, GameManager gm){
        Random rand = new Random();
        this.stat = stat;
        this.color = color;
        this.gm = gm;
        this.coordinates = new Point(rand.nextInt(gm.ui.getWidth() - size),rand.nextInt(gm.ui.getHeight() - (size + 50)));
    }
    public void draw(Graphics g){
        if(i > gm.FPS/8){
            g.setColor(color);
            g.fillRect(coordinates.x,coordinates.y,size,size);
        }
        i++;
        if(i == gm.FPS){
            i = 0;
        }
    }
    public void update(){
        if(hitbox(gm.currentPlayer.coordinates,gm.currentPlayer.size,gm.currentPlayer.size)){
            upgrade();
        }
    }
    private boolean hitbox(Point p2, int w2, int h2) {
        return coordinates.x + size >= p2.x && coordinates.x <= p2.x + w2 && coordinates.y + size >= p2.y && coordinates.y <= p2.y + h2;
    }
    public void upgrade(){
        switch (stat){
            //case "speed" -> gm.currentPlayer.verticalSpeed++;
            case "size" -> gm.currentPlayer.size--;
            case "meteorite" -> {
                if(gm.meteors.size() > 5){
                    gm.meteors.removeFirst();
                }
            }
        }
        gm.upgrades.add(new Upgrade(color,stat,gm));
        gm.upgrades.remove(this);
    }
}
