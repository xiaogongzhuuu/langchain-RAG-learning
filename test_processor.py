from doc_processor import process_markdown_doc

chunks, vectors = process_markdown_doc("docs/openai_api_docs.md")
print(f"共生成 {len(vectors)} 个向量，每个向量维度：{len(vectors[0])}")

print(vectors[0])