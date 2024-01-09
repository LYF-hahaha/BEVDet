from nuscenes.nuscenes import NuScenes

def check_nusc():
    nusc = NuScenes(version='v1.0-mini',
                    dataroot='/root/workspace/BEVDet/data/nusences',
                    verbose=False)
    
    # 某一场景的具体信息
    my_scene = nusc.scene[0]

    # 一个场景的收个sample的token
    first_sample_token = my_scene['first_sample_token']
    
    # 查看第一个场景
    my_sample = nusc.get('sample', first_sample_token)
    
    # 指定sample中的某一传感器
    sensor = 'CAM_FRONT'
    cam_front_data = nusc.get('sample_data', my_sample['data'][sensor])
    # print(cam_front_data)

    # 显示sample的场景
    nusc.render_sample_data(cam_front_data['token'])
    
    
if __name__ == '__main__':
    check_nusc()
