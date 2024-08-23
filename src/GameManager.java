import javax.sound.sampled.*;
import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.util.ArrayList;

public class GameManager {
    ArrayList<Meteor> meteors = new ArrayList<>();
    ArrayList<Upgrade> upgrades = new ArrayList<>();
    public int score = 0;
    Clip music;
    public UI ui;
    KeyListener kl;
    public int FPS = 60;
    public int currentFPS;
    public int screenHeight = 600;
    public int screenWidth = 600;
    public boolean gameIsRunning = true;
    public Player currentPlayer;
    public final static int MENUSTATE = 0;
    public final static int GAMESTATE = 1;
    public final static int GAMEOVERSTATE = 2;
    public static int CURRENTGAMESTATE = GAMESTATE;
    public void start(){
        currentPlayer = new Player(new Point(300,300),Color.RED,this);
        kl = new KeyListener(this);
        ui = new UI(this);
        JFrame frame = new JFrame();
        frame.setSize(screenWidth, screenHeight);
        frame.setTitle("Meteor Crash - Remastered");
        frame.add(ui);
        frame.setVisible(true);
        frame.addKeyListener(kl);
        frame.setFocusable(true);
        upgrades.add(new Upgrade(Color.YELLOW,"meteorite",this));
        //upgrades.add(new Upgrade(Color.BLUE,"speed",this));
        upgrades.add(new Upgrade(Color.MAGENTA,"size",this));
        meteors.add(new Meteor(this));
        meteors.add(new Meteor(this));
        playMusic("src/assets/music/Annihilate.wav");
        framelimiter();
    }
    public void framelimiter() {
        long lastTime = System.currentTimeMillis();
        while (gameIsRunning) {
            long currentTime = System.currentTimeMillis();
            long elapsedTime = currentTime - lastTime;

            if (elapsedTime >= 1000 / FPS) {
                update();
                currentFPS = (int) (1000 / elapsedTime);
                lastTime = currentTime;
            }
            try {
                Thread.sleep(1);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
    int i = 0;
    public void update(){
        i++;
        if(i == FPS){
            score += (meteors.size() * currentPlayer.health);
            i = 0;
        }
        switch (CURRENTGAMESTATE){
            case GameManager.MENUSTATE -> {}
            case GameManager.GAMESTATE -> {
                currentPlayer.update();
                ui.repaint();
                for (int i = 0; i < meteors.size(); i++){
                    meteors.get(i).update();
                }
                for (int i = 0; i < upgrades.size(); i++){
                    upgrades.get(i).update();
                }
            }
            case GameManager.GAMEOVERSTATE -> {}
        }
    }
    public void playMusic(String path){
        if(music != null && music.isActive()){
            stopMusic();
        }
        try{
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(new File(path));
            music = AudioSystem.getClip();
            music.open(audioStream);
            music.start();
        }catch (Exception e){
            System.out.println(e);
        }
    }
    public void stopMusic(){
        if(music.isActive()){
            stopMusic();
        }
    }
}

