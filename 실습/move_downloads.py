import os
import glob
import shutil

# 다운로드 폴더 경로 지정
download_dir = r"C:\Users\student\Downloads"

# 확장자별로 이동할 폴더와 해당 폴더로 이동할 파일 패턴을 딕셔너리로 정의
folders = {
    "images": ["*.jpg", "*.jpeg"],           # 이미지 파일은 images 폴더로
    "data": ["*.csv", "*.xlsx"],             # 데이터 파일은 data 폴더로
    "docs": ["*.txt", "*.doc", "*.pdf"],     # 문서 파일은 docs 폴더로
    "archive": ["*.zip"]                     # 압축 파일은 archive 폴더로
}

# 각 폴더별로 반복
for folder, patterns in folders.items():
    # 다운로드 폴더 하위에 분류 폴더 생성
    target_dir = os.path.join(download_dir, folder)
    # 폴더가 존재하지 않으면 새로 생성
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    # 해당 폴더로 이동할 파일 패턴별로 반복
    for pattern in patterns:
        # 다운로드 폴더에서 해당 패턴에 맞는 파일 목록을 가져옴
        for file in glob.glob(os.path.join(download_dir, pattern)):
            try:
                # 파일을 대상 폴더로 이동
                shutil.move(file, target_dir)
                # 이동 성공 메시지 출력
                print(f"{os.path.basename(file)} → {folder} 폴더로 이동")
            except Exception as e:
                # 이동 실패 시 에러 메시지 출력
                print(f"{os.path.basename(file)} 이동 실패: {e}")