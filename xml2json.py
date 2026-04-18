# XML 转 JSON 标准格式
import xmltodict
import json

def main():
    try:
        with open("./xml/e.xml", "r", encoding="utf-8") as f:
            xml_content = f.read()
        
        # 解析XML
        data = xmltodict.parse(xml_content)
        
        # 写入JSON
        with open("./json/e.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print("✅ XML 转 JSON 完成")
    except Exception as e:
        print(f"❌ 转换失败：{e}")

if __name__ == "__main__":
    main()