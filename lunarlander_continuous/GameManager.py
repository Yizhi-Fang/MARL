# Copyright (c) 2016, NVIDIA CORPORATION. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import gym
from gym.spaces import Box
import numpy as np

class GameManager:
    def __init__(self, game_name, display):
        self.game_name = game_name
        self.display = display

        self.env = gym.make(game_name)
        self.reset()

    def reset(self):
        observation1, observation2 = self.env.reset()
        return observation1, observation2

    def step(self, action1, action2):
        # Yizhi edit here
        self._update_display()

#        print('action1 and 2 :')
#        print(action1)
#        print(action2)

        if isinstance(self.env.action_space, Box):
          action1 = np.clip(action1, self.env.action_space.low, self.env.action_space.high)
          action2 = np.clip(action2, self.env.action_space.low, self.env.action_space.high)
        # need to modify the environment

        observation1, observation2, reward1, reward2, done, info = self.env.step(np.array([action1, action2]))
        return observation1, observation2, reward1, reward2, done, info

    def _update_display(self):
        if self.display:
            self.env.render()
