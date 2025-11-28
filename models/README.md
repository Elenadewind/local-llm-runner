## Models Directory

### How to Get GGUF Models
1. **Hugging Face Model Hub**  
   Search for: `model-name-GGUF` (e.g., `TheBloke/Phi-3-mini-4k-instruct-GGUF`).  

2. **Recommended Sources**  
   - [TheBloke's GGUF repo](https://huggingface.co/TheBloke)  
   - [lm-studio](https://lmstudio.ai/) (GUI for model download)

3. **Naming Convention**  
   Rename downloaded file to: `phi-3-mini.gguf`, `mistral-7b.gguf`, etc.

4. **Placement**  
   Put files directly in this `models/` folder.

### Model Compatibility
| Model | Context | Quantization |
|-------|-------|------------|
| Phi-3 | 4k | Q4_K_M |
| Mistral 7B | 8k | Q5_K_S |
| Llama 2 7B | 4k | Q4_0 |

>  Warning: Models larger than 7B may require >16GB RAM.
