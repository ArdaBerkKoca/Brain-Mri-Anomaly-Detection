from utils.data_loader import get_train_test_generators
from models.autoencoder_model import train_and_evaluate_autoencoder
import matplotlib.pyplot as plt
import os

os.makedirs("results", exist_ok=True)

train_gen, test_gen = get_train_test_generators()
history, auc = train_and_evaluate_autoencoder(train_gen, test_gen, epochs=20)

# Loss grafiği sadece eğitim yapılmışsa çizilsin
if history is not None:
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Val Loss')
    plt.title('Autoencoder Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/autoencoder_loss.png")
    plt.show()
else:
    print("Eğitim yapılmadı, loss grafiği çizilmedi.")


print("Autoencoder ROC AUC:", auc)
