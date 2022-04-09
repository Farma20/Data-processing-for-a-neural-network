import os, shutil

#КОД ЯВЛЯЕТСЯ ВЫПОЛНЕНЫМ, ВСЕ ФАЙЛЫ СКОПИРОВАННЫ

original_dataset_dir = 'C:\\Users\\iurba\\Desktop\\проганье\\Проги\\python\\Глубокое обучение\\Dogs vs Cats\\Dogs vs Cats\\train\\train'

base_dir = "C:\\Users\\iurba\\Desktop\\проганье\\Проги\\python\\Глубокое обучение\\Dogs vs Cats\\Dogs vs Cats\\dogs_vs_cats_small"
os.mkdir(base_dir)

#создаем папки для хранения тренировочных, проверочных и тестовых данных

train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)

validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)

test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

#Создаем внутри папок еще папки dogs и cats

train_cats_dir = os.path.join(train_dir, 'train_cats')
os.mkdir(train_cats_dir)
train_dogs_dir = os.path.join(train_dir, 'train_dogs')
os.mkdir(train_dogs_dir)

validation_cats_dir = os.path.join(validation_dir, 'validation_cats')
os.mkdir(validation_cats_dir)
validation_dogs_dir = os.path.join(validation_dir, 'validation_dogs')
os.mkdir(validation_dogs_dir)

test_cats_dir = os.path.join(test_dir, 'test_cats')
os.mkdir(test_cats_dir)
test_dogs_dir = os.path.join(test_dir, 'test_dogs')
os.mkdir(test_dogs_dir)

#Копируем фотографии в папки
#кошки
fnames = ['cat.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_cats_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['cat.{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(validation_cats_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['cat.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(test_cats_dir, fname)
    shutil.copyfile(src, dst)

#собаки

fnames = ['dog.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_dogs_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['dog.{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(validation_dogs_dir, fname)
    shutil.copyfile(src, dst)

fnames = ['dog.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(test_dogs_dir, fname)
    shutil.copyfile(src, dst)

import os, shutil

base_dir = "C:\\Users\\iurba\\Desktop\\проганье\\Проги\\python\\Глубокое обучение\\Dogs vs Cats\\Dogs vs Cats\\dogs_vs_cats_small"
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')

train_cats_dir = os.path.join(train_dir, 'train_cats')
train_dogs_dir = os.path.join(train_dir, 'train_dogs')

validation_cats_dir = os.path.join(validation_dir, 'validation_cats')
validation_dogs_dir = os.path.join(validation_dir, 'validation_dogs')

test_cats_dir = os.path.join(test_dir, 'test_cats')
test_dogs_dir = os.path.join(test_dir, 'test_dogs')



print('train_cats: ', len(os.listdir(train_cats_dir)))
print('validation_cats: ', len(os.listdir(validation_cats_dir)))
print('test_cats: ', len(os.listdir(test_cats_dir)))

print('train_dogs: ', len(os.listdir(train_dogs_dir)))
print('validation_dogs: ', len(os.listdir(validation_dogs_dir)))
print('test_dogs: ', len(os.listdir(test_dogs_dir)))




















