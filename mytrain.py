from denoising_diffusion_pytorch import Unet, GaussianDiffusion, Trainer
import torch
torch.cuda.empty_cache()

model = Unet(
    dim = 64,
    dim_mults = (1, 2, 4, 8)
)

diffusion = GaussianDiffusion(
    model,
    image_size = 128,
    timesteps = 1000,           # number of steps
    sampling_timesteps = 250,   # number of sampling timesteps (using ddim for faster inference [see citation for ddim paper])
    loss_type = 'l1'            # L1 or L2
)

trainer = Trainer(
    diffusion,
    '../png1/',
    train_batch_size = 32,
    train_lr = 8e-5,
    train_num_steps = 10000,         # [should edit] total training steps
    gradient_accumulate_every = 2,    # gradient accumulation steps
    ema_decay = 0.995,                # exponential moving average decay
    amp = False                        # turn on mixed precision
)

trainer.train()
