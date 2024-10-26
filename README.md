# Handwritten Text Recognition

This  uses the Hugging Face `transformers` model to recognise handwritten text from an uploaded image.

## Setup Instructions
Here is how to test the model and get inferences for your handwritten texts

### 1. Clone the repository

`git clone https://github.com/cyberholic/Hand-Writing-Detection.git`
`cd Hand-Writing-Detection `

### 2. Set up the environment using Conda

`conda env create -f environment.yml`
`conda activate HWR`

### 3. Run the Flask App

After setting up the environment, run the Flask app: `python app.py`

Here’s a comparative table highlighting the key differences between AdCreative and QuickAds:

| **Feature**                   | **AdCreative**                                                                                                                                                                         | **QuickAds**                                                                                                                                                                                                                          |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Flexibility and Editing Capabilities** | Limited customization in editor; users can’t move logos or resize text. Basic editing capabilities restrict more specific design needs.                                         | Full Canva-like editor allowing complete customization, including resizing and moving elements, suitable for both simple and complex designs.                                                                                        |
| **Template Library and Ad Sizes**         | Provides 64 design templates across 8 ad sizes, sufficient for basic use but limiting for varied platform needs.                                                                | Thousands of templates across 31 ad sizes, covering multiple industries and platforms, making it adaptable for various advertising requirements.                                               |
| **AI and Automation**                     | Uses AI mainly for stock image suggestions; lacks deep AI-driven creation features.                                                                                             | Strongly AI-driven; users can input product descriptions or websites to generate hundreds of personalized ad variations. Includes a vast AI-powered ad library by industry and country.                                             |
| **Video Creation**                        | Limited to GIF-style video ads, which restricts diverse or high-quality video content creation.                                                                                 | Supports full natural and animated video creation, including “burst mode” and 15 one-click video variations for rapid production.                                                             |
| **Process Speed and Bulk Creation**       | Good speed but lacks advanced automation; requires manual tweaks for multiple ads.                                                                                              | Faster with “bulk create” features, allowing easy changes across multiple ads, beneficial for agencies or large campaigns.                                                                    |
| **Content Strategy and Ad Library**       | No content strategy or insights library, limiting use for trend-based campaign planning.                                                                                        | Includes Winning Ads Library with weekly updates, categorized by industry and country for strategic insights from Meta and TikTok ads.                                                         |
| **Stock Resources and Custom Media Creation** | Standard premium stock images and AI-generated images; limited control for unique image creation.                                                                               | Access to 135M+ premium images and 59M+ videos; proprietary AI models for generating unique images, providing more visual control.                                                            |
| **Workflow and Campaign Management**      | Lacks campaign management capabilities; requires external tools for publishing and ad campaign management.                                                                      | All-in-one platform with social media scheduling, ad publishing, and campaign management (both automatic and manual settings) for a comprehensive ad workflow.                                 |
| **Output Quality**                        | Good output, suitable for slower-paced content, but less effective for dynamic or attention-grabbing visuals.                                                                   | High output quality, optimized for both slow and fast-paced videos with advanced features like combining images, videos, and dynamic effects for engaging content.
This will start the server, and you can access the app at http://127.0.0.1:5000 in your browser.

### 4. Usage
Navigate to the app, upload an image containing your handwritten text, or use your camera.
The app will return the recognised text.


