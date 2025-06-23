from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_train_test_generators(image_size=(128, 128), batch_size=32):
    dataset_path = "./data/Training"
    test_path = "./data/Testing"

    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        zoom_range=0.2,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True
    )

    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=image_size,
        class_mode='categorical',
        shuffle=True,
        batch_size=batch_size
    )

    test_generator = test_datagen.flow_from_directory(
        test_path,
        target_size=image_size,
        class_mode='categorical',
        shuffle=False,
        batch_size=batch_size
    )

    return train_generator, test_generator
