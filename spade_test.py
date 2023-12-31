"""
Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).
"""

from util import html
from util.visualizer import Visualizer
from models.pix2pix_model import Pix2PixModel
from options.test_options import TestOptions
import data
from collections import OrderedDict
import os
import jittor as jt
from jittor import init
from jittor import nn
jt.flags.use_cuda = 1


opt = TestOptions().parse()

dataloader = data.create_dataloader(opt)

model = Pix2PixModel(opt)
model.eval()

visualizer = Visualizer(opt)

# create a webpage that summarizes the all results
web_dir = os.path.join(opt.results_dir, opt.name,
                       '%s_%s' % (opt.phase, opt.which_epoch))
webpage = html.HTML(web_dir,
                    'Experiment = %s, Phase = %s, Epoch = %s' %
                    (opt.name, opt.phase, opt.which_epoch))

# test
for i, data_i in enumerate(dataloader):
    if i * opt.batchSize >= opt.how_many:
        break
    generated, generated2, generated_edge = model(data_i, mode='inference')
    img_path = data_i['path']
    #import pdb;pdb.set_trace()
    for b in range(generated.shape[0]):
        print('process image... %s' % img_path[b])
        visuals = OrderedDict([('input_label', data_i['label'][b]),
                               ('synthesized_edge', generated_edge[b]),
                               ('synthesized_image', generated2[b]),
                               ])
        visualizer.save_images(webpage, visuals, img_path[b:b + 1])

webpage.save()
