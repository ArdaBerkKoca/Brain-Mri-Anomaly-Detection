from utils.data_loader import get_train_test_generators
from models.one_class_svm_model import train_and_evaluate_one_class_svm
import time

print("One-Class SVM anomaly detection başlatılıyor...\n")
start = time.time()

train_gen, test_gen = get_train_test_generators()
train_and_evaluate_one_class_svm(train_gen, test_gen)

end = time.time()
print(f"\nToplam süre: {end - start:.2f} saniye")
