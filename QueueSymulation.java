import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class QueueSimulation {
    
    // Klasa reprezentująca klienta
    static class Client {
        private final int id;

        public Client(int id) {
            this.id = id;
        }

        public int getId() {
            return id;
        }
    }

    public static void main(String[] args) {
        Queue<Client> queueA = new LinkedList<>();
        Queue<Client> queueB = new LinkedList<>();
        Queue<Client> queueC = new LinkedList<>();

        Random random = new Random();
        int clientId = 1;

        long startTime = System.currentTimeMillis();
        long duration = 60 * 1000; // 60 sekund

        while (System.currentTimeMillis() - startTime < duration) {
            // Losowe przydzielenie klienta do kolejki A, B lub C
            int queueChoice = random.nextInt(3);
            Client client = new Client(clientId++);

            switch (queueChoice) {
                case 0:
                    queueA.add(client);
                    System.out.println("Klient " + client.getId() + " dołączył do kolejki A.");
                    break;
                case 1:
                    queueB.add(client);
                    System.out.println("Klient " + client.getId() + " dołączył do kolejki B.");
                    break;
                case 2:
                    queueC.add(client);
                    System.out.println("Klient " + client.getId() + " dołączył do kolejki C.");
                    break;
            }

            // Obsługa klientów z kolejek
            if (!queueA.isEmpty()) {
                Client servedClient = queueA.poll();
                System.out.println("Obsłużono klienta " + servedClient.getId() + " z kolejki A.");
            }
            if (!queueB.isEmpty()) {
                Client servedClient = queueB.poll();
                System.out.println("Obsłużono klienta " + servedClient.getId() + " z kolejki B.");
            }
            if (!queueC.isEmpty()) {
                Client servedClient = queueC.poll();
                System.out.println("Obsłużono klienta " + servedClient.getId() + " z kolejki C.");
            }

            // Pauza na krótki czas, aby symulacja była bardziej realistyczna
            try {
                Thread.sleep(500); // 500 ms
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        System.out.println("Symulacja zakończona.");
    }
}
