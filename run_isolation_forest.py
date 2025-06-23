from utils.data_loader import get_train_test_generators
from models.isolation_forest_model import train_and_evaluate_isolation_forest
import time

print("Isolation Forest anomaly detection başlatılıyor...\n")
start = time.time()

train_gen, test_gen = get_train_test_generators()
train_and_evaluate_isolation_forest(train_gen, test_gen)

end = time.time()
print(f"\nToplam süre: {end - start:.2f} saniye")
