class Config:
    data_path_train = 'data/train'
    data_path_test = 'data/test'
    data_path_checkpoint ='ckpts'
    model_path_test='denoise_epoch_120.pth'
    denoised_dir =  'final'
    img_channel = 3
    max_epoch = 50
    crop_img_size = 128
    learning_rate = 0.001
    save_per_epoch = 5
    gaussian_noise_param = 30
    test_noise_param = 70
    cuda = "cuda:1"
