#!/usr/bin/env python3
"""
调试脚本：查看botyard_left URDF的关节索引问题
"""

import sapien.core as sapien
import numpy as np

def debug_joint_indices():
    # 创建引擎和场景
    engine = sapien.Engine()
    scene = engine.create_scene()
    
    # 加载URDF
    loader = scene.create_urdf_loader()
    hand = loader.load("./assets/botyard_left/botyard_hand_left.urdf")
    
    # 获取所有活动关节
    all_joints = hand.get_active_joints()
    all_joint_names = [joint.name for joint in all_joints]
    
    print("所有活动关节:")
    for i, name in enumerate(all_joint_names):
        print(f"  索引 {i}: {name}")
    
    # 配置文件中的关节顺序
    config_joint_order = [
        "THJ4", "THJ3", "THJ2", "THJ1",
        "FFJ4", "FFJ3", "FFJ2", "FFJ1",
        "MFJ4", "MFJ3", "MFJ2", "MFJ1",
        "RFJ4", "RFJ3", "RFJ2", "RFJ1",
        "LFJ4", "LFJ3", "LFJ2", "LFJ1"
    ]
    
    print(f"\n配置文件中的关节顺序: {config_joint_order}")
    
    # 检查哪些关节在活动关节列表中
    found_indices = []
    missing_joints = []
    
    for joint_name in config_joint_order:
        if joint_name in all_joint_names:
            idx = all_joint_names.index(joint_name)
            found_indices.append(idx)
            print(f"  ✓ {joint_name} -> 索引 {idx}")
        else:
            missing_joints.append(joint_name)
            print(f"  ✗ {joint_name} -> 未找到")
    
    print(f"\n找到的索引: {found_indices}")
    print(f"缺失的关节: {missing_joints}")
    
    # 检查索引连续性
    if found_indices:
        min_idx = min(found_indices)
        max_idx = max(found_indices)
        expected_range = list(range(min_idx, max_idx + 1))
        
        print(f"\n索引范围: {min_idx} 到 {max_idx}")
        print(f"期望的连续索引: {expected_range}")
        print(f"实际的索引: {found_indices}")
        
        missing_indices = [i for i in expected_range if i not in found_indices]
        if missing_indices:
            print(f"缺失的索引: {missing_indices}")
    
    return found_indices, missing_joints

if __name__ == "__main__":
    debug_joint_indices()