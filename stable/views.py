from django.shortcuts import render

# Create your views here.
# backend/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import torch
from diffusers import WuerstchenDecoderPipeline, WuerstchenPriorPipeline
from diffusers.pipelines.wuerstchen import DEFAULT_STAGE_C_TIMESTEPS

dtype = torch.float32
prior_pipeline = WuerstchenPriorPipeline.from_pretrained("warp-ai/wuerstchen-prior", torch_dtype=dtype)
decoder_pipeline = WuerstchenDecoderPipeline.from_pretrained("warp-ai/wuerstchen", torch_dtype=dtype)
num_images_per_prompt = 1

@csrf_exempt
def generate_image(request):
    if request.method == 'POST':
        try:
            caption = "(Children's Illustration Style),(masterpiece),(cute),mouse in city"
            negative_prompt = 'disfigured'

            prior_output = prior_pipeline(
                prompt=caption,
                height=512,
                width=512,
                timesteps=DEFAULT_STAGE_C_TIMESTEPS,
                negative_prompt=negative_prompt,
                guidance_scale=4.0,
                num_images_per_prompt=num_images_per_prompt,
            )
            decoder_output = decoder_pipeline(
                image_embeddings=prior_output.image_embeddings,
                prompt=caption,
                negative_prompt=negative_prompt,
                guidance_scale=0.0,
                output_type="pil",
            ).images

            image = decoder_output[0]

            # 이미지를 파일로 저장
            save_path = "media/images/bookimage.png"
            image.save(save_path)

            return JsonResponse({'image_path': save_path})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})
