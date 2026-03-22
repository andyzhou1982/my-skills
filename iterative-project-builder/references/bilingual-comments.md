# Bilingual Comment Guidelines

Format for code comments in English + Chinese.

## Python

```python
# Initialize the FastAPI application
# 初始化 FastAPI 应用
app = FastAPI()

def process_document(file: UploadFile) -> Document:
    """
    Process uploaded document and extract text
    处理上传的文档并提取文本

    Args:
        file: Uploaded file object
              上传的文件对象
    Returns:
        Document object with extracted content
        包含提取内容的文档对象
    """
    # Read file content
    # 读取文件内容
    content = await file.read()

    # Extract text based on file type
    # 根据文件类型提取文本
    if file.filename.endswith('.pdf'):
        text = extract_pdf_text(content)
    else:
        text = content.decode('utf-8')

    return Document(content=text)
```

## TypeScript/JavaScript

```typescript
/**
 * Document upload component
 * 文档上传组件
 */
const DocumentUpload: React.FC<Props> = ({ onUpload }) => {
  // State for selected file
  // 选中的文件状态
  const [file, setFile] = useState<File | null>(null)

  // Handle file selection
  // 处理文件选择
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.[0]) {
      setFile(e.target.files[0])
    }
  }

  return (
    // Upload form container
    // 上传表单容器
    <div className="upload-container">
      <input type="file" onChange={handleFileChange} />
    </div>
  )
}
```

## Format Rules

### Inline Comments
```
// English comment
// 中文备注
code here
```

### Block Comments
```python
"""
English description
中文描述

Args/Params:
    param1: English description
            中文描述
"""
```

### Section Headers
```python
# =====================
# Section Name
# 区块名称
# =====================
```

## Key Points

1. **English first** - Always English comment before Chinese
2. **Same line or adjacent** - Keep them visually connected
3. **Match indentation** - Both comments at same level
4. **Be concise** - Don't duplicate obvious information
5. **Document "why" not "what"** - Explain reasoning, not syntax
