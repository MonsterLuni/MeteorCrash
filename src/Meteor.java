import java.awt.*;
import java.util.Random;

public class Meteor {
    Point coordinates;
    int width,height, speedY;
    Color color;
    GameManager gm;
    public Meteor(GameManager gm){
        this.gm = gm;
        Random rand = new Random();
        float r = rand.nextFloat();
        float g = rand.nextFloat();
        float b = rand.nextFloat();
        this.color = new Color(r, g, b);
        this.width = rand.nextInt(100-5) + 5;
        this.height = rand.nextInt(100-5) + 5;
        this.speedY = rand.nextInt(10-2) + 2;
        coordinates = new Point(rand.nextInt(gm.ui.getWidth() - width),-height);
    }
    public void draw(Graphics g){
            g.setColor(color);
            g.fillRect(coordinates.x,coordinates.y,width,height);
    }
    public void update(){
        movement();
        if(hitbox(gm.currentPlayer.coordinates,gm.currentPlayer.size,gm.currentPlayer.size)){
            color = Color.RED;
            gm.currentPlayer.health--;
            if(gm.currentPlayer.health > 0){
                gm.meteors.remove(this);
            }
        }
    }

    private boolean hitbox(Point p2, int w2, int h2) {
        return coordinates.x + width >= p2.x && coordinates.x <= p2.x + w2 && coordinates.y + height >= p2.y && coordinates.y <= p2.y + h2;
    }

    public void movement(){
        if(coordinates.y + speedY > gm.ui.getHeight() + 5 + speedY){
            gm.meteors.add(new Meteor(gm));
            if(Math.random() > 0.8){
                gm.meteors.add(new Meteor(gm));
            }
            gm.meteors.remove(this);
        }else{
            coordinates.y += speedY;
        }
    }
}
