import argparse
import sys
import matplotlib.pyplot as plt
from os.path import dirname, realpath
sys.path.append(dirname(dirname(realpath(__file__))))
from skimage import io

parser = argparse.ArgumentParser(description='DeepTwist Grasp Detection Network')
parser.add_argument('--model', nargs='?', type=str, default='deep_twist') 
args = parser.parse_args()



def main():
    model = model_utils.get_model(args.model)
    train_data, dev_data = load_datasets()
    train_utils.train_model(train_data, dev_data, model, args)
    train_transform = torchvision.transforms.Compose([transforms.CenterCrop(351),
                                                      transforms.RandomRotate(0, 360),
                                                      transforms.CenterCrop(321),
                                                      transforms.RandomTranslate(50),
                                                      transforms.Resize(227)])


    

if __name__ == '__main__':
    main()
