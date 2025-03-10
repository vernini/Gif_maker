#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
여러 하위 폴더의 JPEG 이미지 시퀀스를 GIF 이미지로 일괄 변환하는 프로그램
폴더 구조: test_images/폴더1/폴더2/sequence/시퀀스파일.jpg
출력: test_images/폴더1/폴더2.gif
"""

import os
import argparse
import glob
import re
from PIL import Image

def natural_sort_key(s):
    """숫자를 포함한 문자열을 자연스러운 순서로 정렬하기 위한 키 함수"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def create_gif(input_dir, output_file, duration=100, loop=0, colors=256, resize=None):
    """
    JPEG 이미지 시퀀스를 GIF 이미지로 변환합니다.
    
    Args:
        input_dir (str): JPEG 이미지가 있는 디렉토리 경로
        output_file (str): 출력 GIF 파일 경로
        duration (int): 각 프레임 사이의 시간 간격 (밀리초)
        loop (int): 반복 횟수 (0은 무한 반복)
        colors (int): 색상 수 (2-256)
        resize (tuple): 이미지 크기 조정 (width, height) - None이면 원본 크기 유지
    
    Returns:
        bool: 성공 여부
    """
    # 입력 디렉토리에서 JPEG 이미지 파일 찾기
    image_files = []
    for ext in ['*.jpg', '*.jpeg', '*.JPG', '*.JPEG']:
        image_files.extend(glob.glob(os.path.join(input_dir, ext)))
    
    # 파일이 없으면 오류 메시지 출력
    if not image_files:
        print(f"오류: {input_dir} 디렉토리에 JPEG 이미지가 없습니다.")
        return False
    
    # 파일 이름 기준으로 자연스럽게 정렬
    image_files.sort(key=natural_sort_key)
    print(f"{len(image_files)}개의 이미지 파일을 찾았습니다.")
    
    # 이미지 열기
    frames = []
    for img_file in image_files:
        try:
            img = Image.open(img_file)
            
            # RGB 모드로 변환 (RGBA나 다른 모드일 경우)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # 필요한 경우 이미지 크기 조정
            if resize:
                img = img.resize(resize, Image.Resampling.LANCZOS)
            
            # 이미지를 팔레트 모드로 변환하고 색상 수 제한
            img = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=colors)
            
            frames.append(img)
        except Exception as e:
            print(f"이미지 {img_file} 처리 중 오류 발생: {e}")
    
    if not frames:
        print("처리할 수 있는 이미지가 없습니다.")
        return False
    
    # 출력 디렉토리가 없으면 생성
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # GIF 저장
    try:
        frames[0].save(
            output_file,
            format='GIF',
            append_images=frames[1:],
            save_all=True,
            duration=duration,
            loop=loop,
            optimize=True
        )
        print(f"GIF 파일이 성공적으로 생성되었습니다: {output_file}")
        return True
    except Exception as e:
        print(f"GIF 생성 중 오류 발생: {e}")
        return False

def find_sequence_folders(base_dir):
    """
    기본 디렉토리 내에서 'sequence' 폴더를 찾습니다.
    
    Args:
        base_dir (str): 기본 디렉토리 경로
    
    Returns:
        list: (sequence_path, parent_path, parent_name) 튜플의 리스트
    """
    sequence_folders = []
    
    for root, dirs, files in os.walk(base_dir):
        # 현재 디렉토리의 이름이 'sequence'인지 확인
        if os.path.basename(root).lower() == 'sequence':
            # 상위 디렉토리 경로 (폴더1/폴더2)
            parent_path = os.path.dirname(root)
            
            # 상위 디렉토리가 base_dir의 직계 하위 디렉토리인지 확인
            if parent_path == base_dir:
                continue
                
            # 상위 디렉토리의 이름 (폴더2)
            parent_name = os.path.basename(parent_path)
            
            # 상위 디렉토리의 상위 디렉토리 (폴더1)
            grandparent_path = os.path.dirname(parent_path)
            
            # sequence 폴더, 상위 폴더 경로, 상위 폴더 이름을 저장
            sequence_folders.append((root, grandparent_path, parent_name))
    
    return sequence_folders

def process_all_sequences(base_dir, duration=100, loop=0, colors=256, resize=None):
    """
    지정된 기본 디렉토리 내의 모든 하위 폴더에서 이미지 시퀀스를 찾아 GIF로 변환합니다.
    폴더 구조: base_dir/폴더1/폴더2/sequence/시퀀스파일.jpg
    출력: base_dir/폴더1/폴더2.gif
    
    Args:
        base_dir (str): 기본 디렉토리 경로
        duration (int): 각 프레임 사이의 시간 간격 (밀리초)
        loop (int): 반복 횟수 (0은 무한 반복)
        colors (int): 색상 수 (2-256)
        resize (tuple): 이미지 크기 조정 (width, height) - None이면 원본 크기 유지
    
    Returns:
        int: 성공적으로 생성된 GIF 파일 수
    """
    success_count = 0
    
    # sequence 폴더 찾기
    sequence_folders = find_sequence_folders(base_dir)
    
    if not sequence_folders:
        print(f"경고: {base_dir} 내에서 'sequence' 폴더를 찾을 수 없습니다.")
        return 0
    
    print(f"{len(sequence_folders)}개의 시퀀스 폴더를 찾았습니다.")
    
    # 각 sequence 폴더 처리
    for sequence_path, parent_path, folder_name in sequence_folders:
        # JPEG 파일이 있는지 확인
        has_jpeg = False
        for ext in ['*.jpg', '*.jpeg', '*.JPG', '*.JPEG']:
            if glob.glob(os.path.join(sequence_path, ext)):
                has_jpeg = True
                break
        
        if not has_jpeg:
            print(f"경고: {sequence_path}에 JPEG 이미지가 없습니다. 건너뜁니다.")
            continue
        
        # 출력 GIF 파일 경로 생성
        # 예: test_images/폴더1/폴더2/sequence -> test_images/폴더1/폴더2.gif
        output_file = os.path.join(parent_path, f"{folder_name}.gif")
        
        print(f"\n처리 중: {sequence_path} -> {output_file}")
        
        if create_gif(sequence_path, output_file, duration, loop, colors, resize):
            success_count += 1
    
    return success_count

def main():
    parser = argparse.ArgumentParser(description='여러 하위 폴더의 JPEG 이미지 시퀀스를 GIF로 일괄 변환')
    parser.add_argument('base_dir', help='기본 디렉토리 경로 (예: test_images)')
    parser.add_argument('-d', '--duration', type=int, default=100, help='각 프레임 사이의 시간 간격 (밀리초), 기본값: 100ms')
    parser.add_argument('-l', '--loop', type=int, default=0, help='반복 횟수 (0은 무한 반복), 기본값: 0')
    parser.add_argument('-c', '--colors', type=int, default=256, help='색상 수 (2-256), 기본값: 256')
    parser.add_argument('-r', '--resize', type=str, help='이미지 크기 조정 (예: 640x480)')
    
    args = parser.parse_args()
    
    # 색상 수 검증
    if not 2 <= args.colors <= 256:
        print("색상 수는 2에서 256 사이여야 합니다.")
        return
    
    # 크기 조정 인자 처리
    resize = None
    if args.resize:
        try:
            width, height = map(int, args.resize.lower().split('x'))
            resize = (width, height)
        except ValueError:
            print("크기 형식 오류: WIDTHxHEIGHT 형식으로 입력하세요 (예: 640x480)")
            return
    
    # 모든 시퀀스 처리
    success_count = process_all_sequences(
        args.base_dir,
        duration=args.duration,
        loop=args.loop,
        colors=args.colors,
        resize=resize
    )
    
    print(f"\n작업 완료: {success_count}개의 GIF 파일이 생성되었습니다.")

if __name__ == "__main__":
    main() 