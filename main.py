from PIL import Image, ImageDraw, ImageFont
import random
import string
import streamlit as st
from io import BytesIO

def generate_captcha(text, font_path='arial.ttf', font_size=36):
    width, height = 200, 100
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)