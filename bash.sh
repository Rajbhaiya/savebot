echo "[INFO]: BOT STARTED";
cd /app
rm -rf savebot1
git clone https://github.com/Rajbhaiya/savebot1
cd savebot1
pip install --quiet -r requirements.txt
python3 -m main
