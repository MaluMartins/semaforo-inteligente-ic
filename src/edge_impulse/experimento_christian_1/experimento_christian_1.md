# Experimento 1 - Detecção de Ônibus

## Informações Gerais

- **Autor**: Christian
- **Data**: 28/10/2025
- **Dataset**:
- **Projeto Edge Impulse**: [link aqui]

## Parâmetros

| Parâmetro            | Valor           |
| --------------------- | --------------- |
| Tipo de Modelo        | Classificação |
| Épocas               | =               |
| Resolução da Imagem | 96x96           |
| Profundidade de Cor   | RBG             |
| Data Augmentation     | Não            |
| Taxa de Aprendizado   | 0.001           |

## Métricas

| Métrica  | Resultado |
| --------- | --------- |
| Acurácia | 80.9%     |
| F1-Score  | 0.76      |
| Precisão | 0.72      |
| Recall    | 0.81      |

## Uso no Dispositivo

| Métrica             | Valor     |
| -------------------- | --------- |
| Tempo de Inferência | 603 ms    |
| Pico de uso RAM      | 77,6 KB  |
| Uso de Flash         | 134,3 KB |

## Observações

- Pós processamento utilizado: não.
- Testes com EON Tuner: não.
