import CleanData
import NewData
import CRUDData
import GUI
import FundamentalAnalysis

def main():
    # Lọc dữ liệu (Class CleanData)
    CleanData.CleanData

    # Phát sinh thêm dữ liệu sau khi lọc (NewData)
    NewData.NewData

    CRUDData.CRUDData

    GUI.main()

    FundamentalAnalysis.main()

if __name__ == "__main__":
    main()
