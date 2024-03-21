# -*- coding: UTF-8 -*-


from .byol import BYOL
from models import model_dict


@model_dict.register('byol_sghm_cifar20_r34_org')
class BYOL_CIFAR20_R34(BYOL):
    def cosine_annealing_LR(self, n_iter):
        opt = self.opt

        import math
        epoch = (n_iter - 1) // self.iter_per_epoch
        eta_min = 0
        warmup_from = 0.
        # warmup
        if epoch < opt.warmup_epochs:
            warmup_to = eta_min + (opt.learning_rate - eta_min) * (
                    1 + math.cos(math.pi * opt.warmup_epochs / opt.epochs)) / 2
            p = n_iter / (opt.warmup_epochs * self.iter_per_epoch)
            lr = warmup_from + p * (warmup_to - warmup_from)
        else:
            lr = opt.learning_rate
            lr = eta_min + (lr - eta_min) * (
                    1 + math.cos(math.pi * epoch / opt.epochs)) / 2

        return lr
