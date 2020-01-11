# import tensorflow as tf

#NN_MODEL = "./submit/results/nn_model_ep_18200.ckpt" # model path settings
TARGET_BUFFER = [0.5 , 1.0]
class Algorithm:
     def __init__(self):
     # fill your self params
         self.buffer_size = 0

     # Intial
     def Initial(self):
     # Initail your session or something

     # restore neural net parameters
         self.buffer_size = 0


     #Define your al
     def run(self, time, S_time_interval, S_send_data_size, S_chunk_len, S_rebuf, S_buffer_size, S_play_time_len,S_end_delay, S_decision_flag, S_buffer_flag,S_cdn_flag,S_skip_time, end_of_video, cdn_newest_id,download_id,cdn_has_frame,IntialVars):

         # If you choose the marchine learning
         '''state = []

         state[0] = ...
         state[1] = ...
         state[2] = ...
         state[3] = ...
         state[4] = ...

         decision = actor.predict(state).argmax()
         bit_rate, target_buffer = decison//4, decison % 4 .....
         return bit_rate, target_buffer'''

         # If you choose BBA

         # 阈值
         RESEVOIR = 0.5
         CUSHION =  1.5
         DELAY = 2

         # 参数设置
         # S_buffer_size : 当前时刻缓冲区大小
         # S_end_dalay : 端到端延迟

         # S_cdn_flag S_buffer_flag 效果不明显

         

         if S_buffer_size[-1] < RESEVOIR or S_end_delay[-1] > DELAY or S_buffer_flag[-1] == True or S_rebuf[-1] > 0:
             bit_rate = 0
             target_buffer = 1
         elif (S_buffer_size[-1] >= RESEVOIR + CUSHION and S_buffer_size[-1] < CUSHION + CUSHION) :
             bit_rate = 2
             target_buffer = 0
         elif S_buffer_size[-1] >= CUSHION + CUSHION:
             bit_rate = 3
             target_buffer = 0  
         else:
             bit_rate = 1
             target_buffer = 0

         
         latency_limit = 4

         
        
            

         


         return bit_rate, target_buffer, latency_limit

         # If you choose other
         #......



     def get_params(self):
     # get your params
        your_params = []
        return your_params
