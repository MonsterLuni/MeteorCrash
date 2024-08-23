import java.awt.*;

public class Player {
    Point coordinates;
    int size = 20;
    int horizontalSpeed = 0;
    int verticalSpeed = 0;
    int gravity = 2;
    int health = 2;
    Color color;
    GameManager gm;
    public Player(Point coordinates,Color color,GameManager gm){
        this.coordinates = coordinates;
        this.color = color;
        this.gm = gm;
    }
    public void draw(Graphics g){
        g.setColor(color);
        g.fillRect(coordinates.x,coordinates.y,size,size);
    }
    public void update() {
        movement();
        gravity();
        checkDeath();
    }

    private void checkDeath() {
        if(coordinates.y > gm.ui.getHeight() - 50){
            GameManager.CURRENTGAMESTATE = GameManager.GAMEOVERSTATE;
        }
        if(health < 1){
            GameManager.CURRENTGAMESTATE = GameManager.GAMEOVERSTATE;
        }
    }

    public void movement(){
        if(gm.kl.wPressed){
            coordinates.y -= verticalSpeed + health;
        }
        if(gm.kl.aPressed){
            coordinates.x -= horizontalSpeed + health;
        }
        if(gm.kl.sPressed){
            coordinates.y += verticalSpeed + health;
        }
        if(gm.kl.dPressed){
            coordinates.x += horizontalSpeed + health;
        }
    }
    public void gravity(){
        coordinates.y += gravity;
    }
    
}
