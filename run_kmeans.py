from utils.data_loader import get_train_test_generators
from models.kmeans_model import train_and_evaluate_kmeans
import time

print("KMeans anomaly detection başlatılıyor...\n")
start = time.time()

train_gen, test_gen = get_train_test_generators()
train_and_evaluate_kmeans(train_gen, test_gen)

end = time.time()
print(f"\nToplam süre: {end - start:.2f} saniye")
