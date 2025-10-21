# Experimento 1 - Detecção de Ônibus

## Informações Gerais
- **Autor**: Malu
- **Data**: 20/10/2025
- **Dataset**: https://www.kaggle.com/datasets/samuelayman/bus-dataset (793 imagens de treinamento e 207 imagens de teste)
- **Projeto Edge Impulse**: [link aqui]

## Parâmetros
| Parâmetro | Valor |
|-----------|-------|
| Tipo de Modelo | Detecção de Objetos |
| Épocas | 60 |
| Resolução da Imagem | 96x96 |
| Profundidade de Cor | Grayscale |
| Data Augmentation | Sim |
| Taxa de Aprendizado | 0.001 |

## Métricas
| Métrica | Resultado |
|--------|----------|
| Acurácia | 63.4% (149/235) |
| F1-Score | 0.64 |
| Precisão | 0.65 |
| Recall | 0.64 |


## Uso no Dispositivo
| Métrica | Valor |
|---------|-------|
| Tempo de Inferência | 1257 ms |
| Pico de uso RAM | 119,4 KB |
| Uso de Flash | 81,0 KB |

## Observações
- Pós processamento utilizado: não.
- Testes com EON Tuner: não.